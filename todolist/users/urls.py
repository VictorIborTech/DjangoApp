from django.urls import path
from .views import MyLoginView,RegisterView,MyProfile
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page = 'login'), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path("password-reset/", PasswordResetView.as_view(template_name = "registration/password_reset.html",
                                                      html_email_template_name ='registration/password_reset_email.html'),
                                                        name="password_reset"),
    path("password-reset/done", PasswordResetDoneView.as_view(template_name = "registration/password_reset_done.html"), name="password_reset_done"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"), name="password_reset_complete"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirm.html"), name="password_reset_confirm"),


    path('profile/', MyProfile.as_view(), name='profile'),




]