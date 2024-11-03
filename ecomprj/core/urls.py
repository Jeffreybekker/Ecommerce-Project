from os import name
from django import views
from django.urls import path, include
from core.views import *
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
    
    # Update cart
    path("update-cart/", update_cart, name="update-cart"), # This urlpath must be the same as in the function.js

    # Checkout URL
    path("checkout/<oid>", checkout, name="checkout"),
    
    # PayPal URL
    path("paypal/", include('paypal.standard.ipn.urls')),
    
    # Payment successful
    path("payment-completed/<oid>/", payment_completed_view, name="payment-completed"),
    
    # Payment failed
    path("payment-failed/", payment_failed, name="payment-failed"),
    
    # Dashboard URL
    path("dashboard/", customer_dashboard, name="dashboard"),
    
    # Order Detail URL
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),
    
    # Making Address Default
    path("make-default-address/", make_address_default, name="make-default-address"),
    
    # Wishlist Page
    path("wishlist/", wishlist_view, name="wishlist"),
    
    # Added to Wishlist
    path("add-to-wishlist/", add_to_wishlist, name="add-to-wistlist"),
    
    # Removing from Wishlist
    path("remove-from-wishlist/", remove_wishlist, name="remove-from-wistlist"),
    
    # Contact us
    path("contact/", contact, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),
    
    path("about-us/", about_us, name="about-us"),
    path("purchase-guide/", purchase_guide, name="purchase-guide"),
    path("privacy-policy/", privacy_policy, name="privacy-policy"),
    path("terms-of-service/", terms_of_service, name="terms-of-service"),
    
    # New Routes
    path("save_checkout_info", save_checkout_info, name="save_checkout_info"),
    path("api/create_checkout_session/<oid>/", create_checkout_session, name="api_checkout_session"),
    
]