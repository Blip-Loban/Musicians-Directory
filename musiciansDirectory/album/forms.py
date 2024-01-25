from .models import *
from django.forms import ModelForm
class AlbumForm(ModelForm):
    class Meta:
        model=Album
        fields='__all__'


