from django.urls import path,include
from .views import *
urlpatterns = [

path('add/',AddAlbum.as_view(),name='add_album'),
path('edit/<int:id>',UpdateAlbum.as_view(),name='edit_album'),
path('delete/<int:id>',DeleteAlbum.as_view(),name='delete_album'),

]