from django.urls import path
from .views import userLogin, usersignup, profileCreate, profile, profileedit, userLogout

app_name="account"

urlpatterns = [
    path("login/", userLogin, name="login"),
    path('signup/', usersignup, name="signup"),
    path('logout/', userLogout, name="logout"),
    path('profilecreate/', profileCreate, name="profilecreate"),
    path('profileedit/', profileedit, name="profileedit"),
    path('profile/', profile, name="profile"),
]
