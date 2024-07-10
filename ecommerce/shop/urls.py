from django.urls import path
from . import views

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("item/<int:pk>/", views.item_detail, name="item_detail"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("checkout/", views.checkout, name="checkout"),
    path("add-to-cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path('reduce_quantity/<int:item_id>/', views.reduce_quantity, name='reduce_quantity'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
]
