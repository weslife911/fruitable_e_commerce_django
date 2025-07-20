from django.shortcuts import render, redirect
from .models import Fruits, Category, Testimonial, Cart
from django.db.models import Q
from django.core.mail import send_mail
from decouple import config
from django.db.models import Count

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
    return render(request, "pages/home.html", {"fruits": fruits, "categories": categories, "testimonies": testimonies,})

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
    return render(request, "pages/contact.html")

def product_view(request, pk):
    fruit = Fruits.objects.get(pk=pk)
    fruits = Fruits.objects.all()
    categories = Category.objects.annotate(fruit_count=Count(fruit.category)).all()
    return render(request, "pages/shop_detail.html", {"fruit" : fruit, "fruits": fruits, "categories": categories,})

def cart_view(request):
    carts = Cart.objects.filter(user=request.user)
    if request.method == "POST":
        cart = Cart.objects.get(pk=request.POST.get("cart_id"))
        if request.POST.get("action") == "delete":
            cart.delete()
            return redirect("cart")
        elif request.POST.get("action") == "update":
            print(request.POST)
            # cart.quantity = int(request.POST.get("quantity"))
            # cart.save()
            return redirect("cart")
    return render(request, "pages/cart.html", {"carts": carts})