from django.urls import path
from useradmin.views import *

app_name = "useradmin"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("products/", products, name="products"),
    path("add-product/", add_product, name="add-product"),
]