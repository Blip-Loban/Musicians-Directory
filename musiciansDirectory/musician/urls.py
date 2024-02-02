from django.urls import path,include
from .views import *
urlpatterns = [

path('add/',AddMusician.as_view(),name='add_musician'),
path('edit/<int:id>',UpdateMusician.as_view(),name='edit_musician'),

]