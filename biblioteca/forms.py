from django import forms
from .models import Nacionalidad

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = ['pais', 'nacionalidad']

    pais = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nacionalidad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )