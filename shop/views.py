from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Book, Category
from cart.forms import CartAddProductForm

# Create your views here.
def index(request):
    books = Book.objects.all()[:6]
    category = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context={
        'books':books,
        'category':category,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/index.html', context)

def bookdetail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    context={
        'book':book,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/bookdetail.html', context)

def bookCategory(request, id):
    books = get_list_or_404(Book, category=id)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context={
        'books':books,
        'categories':categories,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/category.html', context)

def allbook(request):
    books = get_list_or_404(Book)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context={
        'books':books,
        'categories':categories,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/category.html', context)