from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("contact/", views.contact_view, name="contact"),
    path("forgot_password/", views.forgot_password_view, name="forgot_password"),
    path("shop/", views.shop_view, name="shop"),
    path("shop/<str:pk>/", views.shop_detail_view, name="shop_detail"),
    path("testimonial/", views.testimonial_view, name="testimonial"),
]