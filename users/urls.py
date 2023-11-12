from django.urls import path
from users.views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signUp/',signup,name='signup-page'),
    path('profile/',profile,name='profile-page'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login-page'),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout-page'),
     path('password_reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html'),
     name='password_reset'),
     path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
     path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

     path('password_reset_complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
