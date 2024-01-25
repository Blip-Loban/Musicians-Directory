from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form= MusicianForm(request.POST)
        if musician_form.is_valid:
            musician_form.save()
            return  redirect('homepage')
    else:
         musician_form= MusicianForm()
    return render(request, 'add_musician.html',{'forms':musician_form})

def edit_musician(request,id):
    form = Musician.objects.get(pk=id)
    musician_form= MusicianForm(instance=form)
    if request.method == 'POST':
        musician_form= MusicianForm(request.POST,instance=form)
        if musician_form.is_valid:
            musician_form.save()
            return  redirect('homepage')
  
    return render(request, 'add_musician.html',{'forms':musician_form})



