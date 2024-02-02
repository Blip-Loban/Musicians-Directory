from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView,UpdateView
# Create your views here.

# def add_album(request):
#     if request.method == 'POST':
#         album_form=AlbumForm(request.POST)
#         if album_form.is_valid:
#             album_form.save()
#             return redirect('homepage')
#     else:
#          album_form=AlbumForm()
#     return render (request, 'add_album.html',{'forms':album_form})

# def edit_album(request,id):
#     form=Album.objects.get(pk=id)
#     album_form=AlbumForm(instance=form)
#     if request.method == 'POST':
#         album_form=AlbumForm(request.POST,instance=form)
#         if album_form.is_valid:
#             album_form.save()
#             return redirect('homepage')
    
#     return render (request, 'add_album.html',{'forms':album_form})

# def delete_album(request,id):
#     album=Album.objects.get(pk=id)
#     album.delete()
#     return redirect('homepage')

class AddAlbum(CreateView):
    template_name='add_album.html'
    model=Album
    form_class=AlbumForm
    success_url=reverse_lazy('homepage')


class UpdateAlbum(UpdateView):
    model =Album
    template_name='add_album.html'
    pk_url_kwarg='id'
    form_class=AlbumForm
    success_url=reverse_lazy('homepage')
class DeleteAlbum(DeleteView):
    model = Album
    pk_url_kwarg='id'
    template_name='delete.html'
    success_url=reverse_lazy('homepage')
