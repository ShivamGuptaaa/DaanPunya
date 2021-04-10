from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.utils.translation import gettext, gettext_lazy

urlpatterns = [
    path("",views.index,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("term/",views.term,name="term"),
    path("medView/<int:id>",views.medView,name="medView"),
    path("searchResult/",views.searchResult,name="searchResult"),
    path("status/",views.status,name="status"),
    path("status1/",views.status1,name="status1"),
    path("status/<int:rq_med_id>",views.status,name="status"),
    path("status1/<int:rq_med_id>",views.status1,name="status1"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("orgRegister/",views.orgRegister,name="orgRegister"),
    path("handleRegister",views.handleRegister,name="handleRegister"),
    path("handleOrgRegister",views.handleOrgRegister,name="handleOrgRegister"),
    path("handleLogin",views.handleLogin,name="handleLogin"),
    path("handleLogout",views.handleLogout,name="handleLogout"),
    path("donateMed/",views.donateMed,name="donateMed"),
    path("handleOtp",views.handleOtp,name="handleOtp"),
    path("rqMed/",views.rqMed,name="rqMed"),
    path("sendAddress/<int:id>",views.sendAddress,name="sendAddress"),
    path("medRcvd/<int:id>",views.med_rcvd,name="medRcvd"),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="webapp/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="webapp\password_reset_mail_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="webapp/password_change.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="webapp/password_reset_done.html"),name="password_reset_complete"),



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 