from django.shortcuts import render, redirect
from fruits.models import Category, Fruits, Testimonial

# Create your views here.
def admin_dashboard_view(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
        return redirect("home")
    elif request.user.is_authenticated == False:
        return redirect("home")
    return render(request, "pages/admin/dashboard.html")

def admin_add_product_view(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
        return redirect("home")
    elif request.user.is_authenticated == False:
        return redirect("home")
    categories = Category.objects.all()
    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get("category"))
        if category:
            fruit = Fruits.objects.create(
                name=request.POST.get("name"),
                category=category,
                price=request.POST.get("price"),
                image=request.FILES.get("image"),
                rating=request.POST.get("rating"),
                description=request.POST.get("description")
            )
            if fruit:
                return redirect("add_product")

    return render(request, "pages/admin/add_product.html", {"categories": categories})

def admin_products_view(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
        return redirect("home")
    elif request.user.is_authenticated == False:
        return redirect("home")
    products = Fruits.objects.all()
    return render(request, "pages/admin/view_products.html", {"products": products})

def admin_edit_product(request, pk):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("home")
    
    product = Fruits.objects.get(pk=pk)
    
    if request.method == "POST":
        category_name = request.POST.get("category")
        
        category, created = Category.objects.get_or_create(category=category_name)
        
        product.name = request.POST.get("name")
        product.category = category
        product.price = request.POST.get("price")
        product.image = request.FILES.get("image")
        product.description = request.POST.get("description")
        product.rating = request.POST.get("rating")
        product.save()
        
        return redirect("products")
    
    return render(request, "pages/admin/edit_products.html", {"product": product})

def admin_delete_product(request, pk):
    product = Fruits.objects.get(pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products")
    
def admin_add_testimony(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
        return redirect("home")
    elif request.user.is_authenticated == False:
        return redirect("home")
    if request.method == "POST":
        testimony = Testimonial.objects.create(
            name=request.POST.get("name"),
            profession=request.POST.get("profession"),
            profile_pic=request.FILES.get("profile_pic"),
            testimony=request.POST.get("testimony")
        )
        if testimony:
            return redirect("products")
    return render(request, "pages/admin/add_testimony.html")