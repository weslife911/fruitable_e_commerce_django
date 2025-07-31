from django.contrib import admin
from .models import Fruits, Testimonial, Category, Cart

# Register your models here.
admin.site.register(Fruits)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Testimonial)