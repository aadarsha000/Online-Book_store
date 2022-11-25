from django.shortcuts import render, get_object_or_404
from .models import Book, Category
# Create your views here.
def index(request):
    books = Book.objects.all()[:6]
    category = Category.objects.all()
    context={
        'books':books,
        'category':category,
    }
    return render(request, 'shop/index.html', context)

def bookdetail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug)
    context={
        'book':book,
    }
    return render(request, 'shop/bookdetail.html', context)