from django.urls import path

from .import views


urlpatterns = [

   path('automotive',views.automotive,name='automotive'),

   path('industryauto',views.industryauto,name='industryauto'),

   path('mobile',views.mobile,name='mobile'),

   path('website',views.website,name='website'),

]

