from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.admin_dashboard_view, name="dashboard"),
    path("add_product/", views.admin_add_product_view, name="add_product"),
    path("products", views.admin_products_view, name="products"),
    path("edit_product/<str:pk>/", views.admin_edit_product, name="edit_product"),
    path("delete_product/<str:pk>/", views.admin_delete_product, name="delete_product"),
    path("add_testimony/", views.admin_add_testimony, name="add_testimony"),
]
