from django.urls import path

from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [

    path('logcon', views.logcon, name='logcon'),

    path('logging', views.logging, name='logging'),

    path('registration_view', views.registration_view, name='registration_view'),

    path('login', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),

    path('logout', auth_views.LogoutView.as_view(template_name='User/logout.html'), name='logout'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='User/password_reset.html'), name= "password_reset"),

    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='User/password_reset_sent.html'),name="password_reset_done"),

    path('reset/<slug:uidb64>/<slug:token>', auth_views.PasswordResetConfirmView.as_view(template_name='User/password_reset_form.html'),name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='User/password_reset_done.html'),name="password_reset_complete"),


    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='User/password_change.html'), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='User/password_change_done.html'), name='password_change_done'),

    path('sendmail', views.sendmail,name="sendmail"),

    path('profile', views.profile, name="profile"),


]

