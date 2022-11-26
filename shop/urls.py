from django.urls import path
from .views import index, bookdetail, bookCategory, allbook
app_name = "shop"
urlpatterns = [
    path('', index, name='index'),
    path('book/<int:id>/<slug:slug>/', bookdetail, name='bookdetail'),
    path('category/<int:id>',bookCategory, name="category"),
    path('allboook/', allbook, name="allbook"),
]
