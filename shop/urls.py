from django.urls import path
from .views import index, bookdetail, bookCategory
app_name = "shop"
urlpatterns = [
    path('', index, name='index'),
    path('book/<int:id>/<slug:slug>/', bookdetail, name='bookdetail'),
    path('category/<int:id>',bookCategory, name="category")
]
