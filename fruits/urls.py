from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_view, name="home"),
    path("contact/", views.contact_view, name="contact"),
    path("product/<str:pk>/", views.product_view, name="product_detail"),
    path("cart/", views.cart_view, name="cart"),
    path("testimonials/", views.testimonial_view, name="testimonials")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)