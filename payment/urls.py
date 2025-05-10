from django.urls import path

from .import views



urlpatterns = [

    path('payment/<int:x>', views.payment, name='payment'),

    path('process',views.payment_process,name='process'),

    path('complete',views.complete, name='complete'),

    path('canceled',views.payment_canceled,name='canceled'),

    path('Cancelpay/<int:x>',views.Cancelpay,name='Cancelpay'),

    path('paycomplete/<int:x>',views.paycomplete,name='paycomplete'),

]
