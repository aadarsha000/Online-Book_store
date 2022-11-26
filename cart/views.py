from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Book
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
        quantity=cd['quantity'],
        override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required(login_url="account:login")
def cart_checkout(request):
    cart = Cart(request)
    return render(request, 'cart/checkout.html', {'cart': cart})

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:thanks')

def thank_you(request):
    return render(request, 'cart/thanks.html')


