from django.urls import path
from cart import views


app_name = "cart"
urlpatterns = [
    path(
            'add-to-cart/<int:product_id>', 
            views.add_product_to_cart, 
            name='add_to_cart'
    ),
]