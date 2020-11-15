from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("medView/<int:id>",views.medView,name="medView"),
    path("searchResult/",views.searchResult,name="searchResult"),
    path("status/",views.status,name="status"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("handleRegister",views.handleRegister,name="handleRegister"),
    path("handleLogin",views.handleLogin,name="handleLogin"),
    path("handleLogout",views.handleLogout,name="handleLogout"),
    path("donateMed/",views.donateMed,name="donateMed"),
    ]