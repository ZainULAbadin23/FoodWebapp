from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from .views import (
    contact_us,
    home,
    ProductList,
    ProductDetailView,
    CartListView,
    MyCart,
    add_item_to_cart,
    remove_item_from_cart,
    customer_order_create,
    my_order_list,
    )

urlpatterns = [
    path('', home, name="home"),
    # path(
    #     "logout/",
    #     LogoutView.as_view(
    #         template_name="user/logout.html",
    #         next_page=reverse_lazy("/")
    #     ),
    #     name="logout",
    # ),
    path('products/', ProductList.as_view(), name='customer-product-list'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(),
         name='customer-product-detail'),
    path('cart/add/', add_item_to_cart, name="add-cart-item"),
    path('cart/delete/<int:product_id>', remove_item_from_cart,
         name="item-delete-cart"),
    path('order/checkout/', CartListView.as_view(), name="checkout"),
    path('order/complete/',
         customer_order_create, name="customer-order-complete"),
         path('order/complete/',
         my_order_list, name="my-order-list"),
    path('contact-us/', contact_us, name='contact-us'),
]
