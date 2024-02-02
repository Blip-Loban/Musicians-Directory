from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView, DeleteView
# Create your views here.
# def add_musician(request):
#     if request.method == 'POST':
#         musician_form= MusicianForm(request.POST)
#         if musician_form.is_valid:
#             musician_form.save()
#             return  redirect('homepage')
#     else:
#          musician_form= MusicianForm()
#     return render(request, 'add_musician.html',{'forms':musician_form})

# def edit_musician(request,id):
#     form = Musician.objects.get(pk=id)
#     musician_form= MusicianForm(instance=form)
#     if request.method == 'POST':
#         musician_form= MusicianForm(request.POST,instance=form)
#         if musician_form.is_valid:
#             musician_form.save()
#             return  redirect('homepage')
  
#     return render(request, 'add_musician.html',{'forms':musician_form})


class AddMusician(CreateView):
    model = Musician
    form_class=MusicianForm
    success_url=reverse_lazy('homepage')
    template_name='add_musician.html'

class UpdateMusician(UpdateView):
    model = Musician
    form_class =MusicianForm
    template_name='add_musician.html'
    pk_url_kwarg='id'
    success_url=  reverse_lazy('homepage')
    

    