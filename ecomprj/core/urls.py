from django.urls import path
from core.views import index, delete_item_from_cart, cart_view, product_list_view, category_list_view, category_product_list_view, vendor_list_view, vendor_detail_view, product_detail_view, tag_list, ajax_add_review, search_view, filter_product, add_to_cart

app_name = "core"

urlpatterns = [
    # homepage
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("products/<pid>", product_detail_view, name="product-detail"),
    
    # Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>", category_product_list_view, name="category-product-list"),
    
    # Vendor
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>", vendor_detail_view, name="vendor-detail"),
    
    # Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
    
    # Add review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),
    
    # Search
    path("search/", search_view, name="search"),
    
    # Filter product URL
    path("filter-products/", filter_product, name="filter-product"),
    
    # Add to cart URL
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    
    # Cart page URL
    path("cart/", cart_view, name="cart"),
    
    # Delete item from cart
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),

]