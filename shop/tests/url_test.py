from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import index, bookdetail, bookCategory, allbook

class TestUrls(SimpleTestCase):
     
    def test_index_urls_resolved(self):
        url = reverse('index')
        print(resolve(url))