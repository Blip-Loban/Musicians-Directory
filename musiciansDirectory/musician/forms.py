from django.forms import ModelForm
from .models import *

class MusicianForm(ModelForm):
    class Meta:
        model=Musician
        fields='__all__'
        