from django.urls import path
from .views import index
app_name = "shop"
urlpatterns = [
    path('', index, name='index'),
]
