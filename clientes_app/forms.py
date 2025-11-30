from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # Usamos los nuevos nombres
        fields = ['documento', 'nombres', 'apellidos', 'correo', 'celular', 'ubicacion']
        widgets = {
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CC o NIT'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }