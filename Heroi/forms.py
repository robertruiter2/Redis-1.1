from django import forms
from .models import Heroi

class HeroiForm(forms.ModelForm):
    class Meta:
        model = Heroi
        fields = ['nome', 'universo', 'habilidade']