from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form=AlbumForm(request.POST)
        if album_form.is_valid:
            album_form.save()
            return redirect('homepage')
    else:
         album_form=AlbumForm()
    return render (request, 'add_album.html',{'forms':album_form})

def edit_album(request,id):
    form=Album.objects.get(pk=id)
    album_form=AlbumForm(instance=form)
    if request.method == 'POST':
        album_form=AlbumForm(request.POST,instance=form)
        if album_form.is_valid:
            album_form.save()
            return redirect('homepage')
    
    return render (request, 'add_album.html',{'forms':album_form})
