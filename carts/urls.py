from django.urls import path

from .views import cart, add_to_cart, remove_from_cart, clear_cart

urlpatterns = [
    path('carts/', cart, name='cart'),
    path('carts/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('carts/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('carts/clear/', clear_cart, name='clear_cart'),
]
