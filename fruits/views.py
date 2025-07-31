from django.shortcuts import render, redirect
from .models import Fruits, Category, Testimonial, Cart
from django.db.models import Q
from django.core.mail import send_mail
from decouple import config
from django.db.models import Count
from decimal import Decimal

# Create your views here.
def home_view(request):
    fruits = Fruits.objects.filter(
        Q(name__icontains=request.GET.get("search", "")) | 
        Q(category__category__icontains=request.GET.get("search", ""))
    )
    categories = Category.objects.all()
    testimonies = Testimonial.objects.all()
    q = request.GET.get("search")
    if request.method == "POST":
        cart = Cart.objects.create(
            user=request.user,
            fruit=Fruits.objects.get(pk=request.POST.get("fruit_id")),
            quantity=1
        )
        if cart:
            return redirect("cart")
    cart = Cart.objects.filter(user=request.user.id)
    return render(request, "pages/home.html", {"fruits": fruits, "categories": categories, "testimonies": testimonies, "cart": cart})

def contact_view(request):
    if request.method == "POST":
        send_mail(
            request.POST.get("subject"),
            request.POST.get("message"),
            request.POST.get("email"),
            [config("RECEIVER_EMAIL")],
            fail_silently=False
        )
        return redirect("home")
    cart = Cart.objects.filter(user=request.user)
    return render(request, "pages/contact.html", {"cart": cart})

def product_view(request, pk):
    fruit = Fruits.objects.get(pk=pk)
    fruits = Fruits.objects.all()
    categories = Category.objects.annotate(fruit_count=Count(fruit.category)).all()
    return render(request, "pages/shop_detail.html", {"fruit" : fruit, "fruits": fruits, "categories": categories,})

def cart_view(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        if request.method == "POST":
            cart = Cart.objects.get(pk=request.POST.get("cart_id"))
            if request.POST.get("action") == "delete":
                cart.delete()
                return redirect("cart")
            elif request.POST.get("action") == "update":
                if request.POST.get("quantity") == 0:
                    cart.delete()
                else:
                    cart.quantity = request.POST.get("quantity")
                    cart.save()
        grand_total = Decimal('0.00')
        for item in carts:
            grand_total += item.total_price
        cart = Cart.objects.filter(user=request.user)
        return render(request, "pages/cart.html", {"carts": carts, "cart": cart, "grand_total": grand_total,})
    else:
        return redirect("login")
    
    
def testimonial_view(request):
    testimonies = Testimonial.objects.all()
    return render(request, "pages/testimonial.html", {"testimonies": testimonies})
