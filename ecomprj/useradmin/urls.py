from django.urls import path
from useradmin.views import *

app_name = "useradmin"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("products/", products, name="products"),
    path("add-product/", add_product, name="add-product"),
    path("edit-product/<pid>/", edit_product, name="edit-product"),
    path("delete-product/<pid>/", delete_product, name="delete-product"),
    path("orders/", orders, name="orders"),
    path("order-detail/<id>/", order_detail, name="order-detail"),
    path("change-order-status/<id>/", change_order_status, name="change-order-status"),
]