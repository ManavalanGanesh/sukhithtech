from django.urls import path
from .import views

urlpatterns=[
	path('clients',views.clients,name='clients'),
]
