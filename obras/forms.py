from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from obras.models import Avatar, Libro

#class FormLibro(forms.Form):
  #  titulo = forms.CharField(max_length=255)
  #  autor = forms.CharField(max_length=255)
  #  descripcion = forms.CharField(widget=forms.Textarea)
   # año = forms.IntegerField()

class FormLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'año', 'portada']

class FormNoticia(forms.Form):
    titulo = forms.CharField(max_length=255)
    autor = forms.CharField(max_length=255)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField()

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ['user', 'imagen']
