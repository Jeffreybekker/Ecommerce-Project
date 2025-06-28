from django.urls import path
from useradmin.views import dashboard, products, add_product, edit_product, delete_product, orders, order_detail, change_order_status, shop_page, reviews, settings, change_password

app_name = "useradmin"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("products/", products, name="products"),
    path("add-product/", add_product, name="add-product"),
    path("edit-product/<pid>/", edit_product, name="edit-product"),
    path("delete-product/<pid>/", delete_product, name="delete-product"),
    path("orders/", orders, name="orders"),
    path("order-detail/<id>/", order_detail, name="order-detail"),
    path("change-order-status/<oid>/", change_order_status, name="change-order-status"),
    path("shop-page/", shop_page, name="shop-page"),
    path("reviews/", reviews, name="reviews"),
    path("settings/", settings, name="settings"),
    path("change-password/", change_password, name="change-password"),
]
