from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Profile

# Create your views here.

def usersignup(request):
    context={}
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("account:profilecreate")
        else:
            context['form']=form
    else:
        form = UserRegistrationForm()
        context['form']=form
    return render(request, "account/signup.html", context)


def userLogin(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("shop:index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = UserLoginForm()
    return render(request, 'account/login.html', {'form':form})

def userLogout(request):
    logout(request)
    return redirect("shop:index")


def profileCreate(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("shop:index")
        else:
            form = ProfileForm(request.POST)
    form = ProfileForm()
    return render(request, 'account/profileedit.html', {'form':form})

def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'account/profile.html', {'profile':profile})


def profileedit(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.save()
            return redirect("account:profile")
    
    form = ProfileForm(instance=profile)
    return render(request, 'account/profileedit.html', {'form':form})
