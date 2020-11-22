from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("medView/<int:id>",views.medView,name="medView"),
    path("searchResult/",views.searchResult,name="searchResult"),
    path("status/",views.status,name="status"),
    path("status1/",views.status1,name="status"),
    path("status/<int:rq_med_id>",views.status,name="status1"),
    path("status1/<int:rq_med_id>",views.status1,name="status1"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("handleRegister",views.handleRegister,name="handleRegister"),
    path("handleLogin",views.handleLogin,name="handleLogin"),
    path("handleLogout",views.handleLogout,name="handleLogout"),
    path("donateMed/",views.donateMed,name="donateMed"),
    path("handleOtp",views.handleOtp,name="handleOtp"),
    path("rqMed/",views.rqMed,name="rqMed"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)