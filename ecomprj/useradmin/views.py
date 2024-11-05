from django.shortcuts import render, redirect
from core.models import CartOrder, Product, Category
from django.db.models import Sum
from userauths.models import User

import datetime

def dashboard(request):
    revenue = CartOrder.objects.aggregate(price=Sum("price"))
    total_orders_count = CartOrder.objects.all()
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    new_customers = User.objects.all(). order_by("-id")
    latest_orders = CartOrder.objects.all()
    
    this_month = datetime.datetime.now().month
    
    monthly_revenue = CartOrder.objects.filter(order_date__month=this_month).aggregate(price=Sum("price"))
    
    context = {
        "revenue": revenue,
        "total_orders_count": total_orders_count,
        "all_products": all_products,
        "all_categories": all_categories,
        "new_customers": new_customers,
        "latest_orders": latest_orders,
        "monthly_revenue": monthly_revenue,
    }
    
    return render(request, "useradmin/dashboard.html", context)


def product(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    
    context = {
        "all_products": all_products,
        "all_categories": all_categories,
        }
    
    return render(request, "useradmin/products.html", context)