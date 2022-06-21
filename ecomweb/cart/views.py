from urllib import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .cart import Cart

from product.models import Product
from django.urls import reverse

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'carts/menu_cart.html')

def cart(request):
    return render(request, 'carts/cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']

    item = {
        'product': {
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'get_thumbnail': product.get_thumbnail(),
            'price': product.price
        },
        'total_price': (quantity * product.price),
        'quantity': quantity,

    }
    response = render(request, 'carts/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response

@login_required
def checkout(request):
    return render(request, 'carts/checkout.html')

def hx_menu_cart(request):
    return render(request, 'carts/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'carts/partials/cart_total.html')


