from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'address', 'image', 'phone_number']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'birth_date' : forms.DateInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'year-month-date'}),
            'gender' : forms.Select(attrs={'class':'form-control form-control-lg'}),
            'nationality' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'address' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            # 'image' : forms.FileInput(attrs={'class':'form-control form-control-lg'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
        }

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = "__all__"

