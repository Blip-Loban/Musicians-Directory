from django.urls import path,include
from .views import *
urlpatterns = [

path('add/',add_album,name='add_album'),
path('edit/<int:id>',edit_album,name='edit_album'),
path('delete/<int:id>',delete_album,name='delete_album'),

]