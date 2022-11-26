from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    Gender_Choice = (
        ("Male","male"),
        ("Female","Female"),
        ("Other","Other"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=Gender_Choice, null=True, blank=True)
    image = models.ImageField(upload_to="images/account/%Y/%m/%d", default="images/account/default.jpg")

    def __str__(self):
        return self.user.username
    

