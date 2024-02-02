from typing import Any
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView, CreateView
from user.models import CustomUser
from franchise.models import Cart, Order
# from django.views.generic.edit import FormView, CreateView


from resturant.models import Product, ProductCategory

from user.decorators import (manager_required,
                             customer_required,
                             staff_required,
                             deliverer_required,
                             resturant_required,
                             admin_required)

# Create your views here.


def home(request, *args, **kwargs):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'customer/index.html', context)


def contact_us(request, *args, **kwargs):
    context = {
        'title': 'contact us',
    }
    return render(request=request,
                  template_name='customer/contact_us.html',
                  context=context
                  )


# @method_decorator([login_required, resturant_required], name="dispatch")
class ProductList(ListView):
    model = Product
    context_object_name = "products"
    template_name = "product/product_list.html"
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context["products"] = products
        context["title"] = "Resturant Dashboard"
        context["product_open"] = True
        context["items_open"] = True
        return context


# @method_decorator([login_required, resturant_required], name="dispatch")
class ProductDetailView(DetailView):

    model = Product
    context_object_name = "product"
    template_name = "product/detail.html"

    def get_context_data(self, **kwargs):
        print(kwargs['object'])
        context = super().get_context_data(**kwargs)
        context["product"] = kwargs['object']
        print(context["product"].sale_price)
        context["title"] = "Products"
        context["product_open"] = True
        return context


class CartListView(ListView):

    model = Cart
    context_object_name = "product"
    template_name = "orders/my_cart.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(customer_id=self.request.user).all()

        context["carts"] = cart
        context["title"] = "My Cart"
        # update = Cart.objects.get(customer_id=self.request.user, item=item)
        # update.quantity = q
        # update.save()
        return context


@method_decorator([login_required, customer_required], name="dispatch")
class MyCart(ListView):

    template_name = "orders/cart.html"
    context_object_name = "cart"
    model = Cart

    # def get_queryset(self):
    #     items = Cart.objects.filter(
    #         customer_id=self.request.user
    #         ).select_related('item')
    #     print(items)
    #     object_list = []
    #     for ob in items:
    #         obj = ob.item
    #         object_list.append({'food_name': obj.food_name, 'price': obj.price,
    #                             'quantity': ob.quantity, 'id': ob.pk})
    #     print(object_list)
    #     return object_list

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["items"] = Cart.objects.filter(
            customer_id=self.request.user
            ).select_related('item')

        object_list = []
        for ob in context["items"]:
            obj = ob.item
            object_list.append({'food_name': obj.food_name, 'price': obj.price,
                                'quantity': ob.quantity, 'id': ob.pk})
        context["object_list"] = object_list
        print("-------items --------")
        print(context["items"])
        return context


@login_required
@customer_required
def add_item_to_cart(request, *args, **kwargs):
    
    if (request.method == 'POST'):
        print("-------cart post-------")
        product_id = request.POST.get("product_id")
        customer = request.user
        product_quantity = 1
    cart = Cart.objects.filter(
        Q(customer_id=customer)).all()
    print(cart)
    item = Product.objects.get(id=product_id)
    if not Cart.objects.filter(customer_id=request.user, item=item).exists():
        print("----------if running---------")
        adding = Cart.objects.create(customer_id=customer,
                                     item=item, quantity=product_quantity)
        adding.save()
    else:
        print("----------else running-------")
        update = Cart.objects.get(customer_id=request.user, item=item)
        update.quantity += 1
        update.save()
        print(update.quantity)

    context = {
        'title': 'add item',
        'carts': cart,
    }

    return redirect(reverse_lazy("checkout"), context=context)


@login_required
@customer_required
def remove_item_from_cart(request, product_id):

    if (request.method == 'POST'):
        print("-------cart delete-------")
        print(product_id)
        Cart.objects.filter(
            item__in=Product.objects.filter(id=product_id)).delete()
    context = {
        'title': 'delete page'
    }
    return redirect(reverse_lazy("checkout"))


@login_required
@customer_required
def customer_order_create(request, *args, **kwargs):
    cart = Cart.objects.filter(customer_id=request.user).all()
    if (request.method == 'POST'):
        print("-----order completed post-----")
    context = {
        'carts': cart

    }
    return render(request=request,
                  template_name="orders/order_complete.html", context=context)


@login_required
@customer_required
def my_order_list(request, *args, **kwargs):
    order = Order.objects.filter(customer_id=request.user).all()
    if (request.method == 'POST'):
        print("-----order completed post-----")
        Order.objects.create(
            
        )
    context = {
        'orders': order

    }
    return render(request=request,
                  template_name="orders/my_order_list.html", context=context)