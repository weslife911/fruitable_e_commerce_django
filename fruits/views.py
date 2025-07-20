from django.shortcuts import render, redirect
from .models import Fruits, Category, Testimonial
from django.db.models import Q
from django.core.mail import send_mail
from decouple import config

# Create your views here.
def home_view(request):
    fruits = Fruits.objects.filter(
        Q(name__icontains=request.GET.get("search", "")) | 
        Q(category__category__icontains=request.GET.get("search", ""))
    )
    categories = Category.objects.all()
    testimonies = Testimonial.objects.all()
    q = request.GET.get("search")
    return render(request, "pages/home.html", {"fruits": fruits, "categories": categories, "testimonies": testimonies})

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
    return render(request, "pages/shop_detail.html", {"fruit" : fruit})