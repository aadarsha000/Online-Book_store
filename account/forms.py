from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"