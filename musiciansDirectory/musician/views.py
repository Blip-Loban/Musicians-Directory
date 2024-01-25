from django.shortcuts import render,redirect
from .forms import *
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


