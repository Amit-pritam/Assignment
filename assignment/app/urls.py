from django.urls import path,include
from .views import *

urlpatterns = [
  path('',home_view,name = 'home'),
  path('country/',addcountry,name = 'country'),
  path('state/',addstate,name = 'state'),
  path('city/',addcity,name = 'city'),
  path('location/',addlocation,name = 'Location'),
  path('result/',submit,name = 'result')
]




