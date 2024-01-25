from django.urls import path,include
from .views import *
urlpatterns = [

path('add/',add_musician,name='add_musician'),

]