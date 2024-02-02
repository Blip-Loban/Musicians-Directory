from django.shortcuts import render
from album.models import Album
from django.views.generic import ListView
# def home(request):
#     albums= Album.objects.all()
#     return render (request, 'home.html',{'albums': albums})
class AlbumView(ListView):
    model = Album
    template_name='home.html'