from django import forms

class FormLista(forms.Form):
    titulo = forms.CharField(max_length=255)
    genero = forms.CharField(max_length=255)
    libros = forms.CharField(widget=forms.Textarea)
    posteador = forms.CharField(max_length=255)
