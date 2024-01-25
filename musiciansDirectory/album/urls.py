from django.urls import path,include
from .views import *
urlpatterns = [

path('add/',add_album,name='add_album'),
path('edit/<int:id>',edit_album,name='edit_album'),

]