from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="images/account/%Y/%m/%d", default="images/account/default.jpg")

    def __str__(self):
        return self.user.username
    

