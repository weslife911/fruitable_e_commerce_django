from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
                    return redirect("home")
        return render(request, "pages/login.html")

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = UserRegistrationForm()
        errors = None
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("home")
            errors = form.errors;
        return render(request, "pages/register.html", {"errors": errors})
    
def logout_user(request):
    logout(request)
    return redirect("home")

def forgot_password_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            print(request.POST)
        return render(request, "pages/forgot_password.html")