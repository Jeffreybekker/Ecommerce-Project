from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address


# Create your views here.
def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True)
    
    context = {
        "products": products,
    }
    
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    
    context = {
        "products": products,
    }
    
    return render(request, 'core/product-list.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    
    context = {
        "categories": categories,
    }
    
    return render(request, 'core/category-list.html', context)
    