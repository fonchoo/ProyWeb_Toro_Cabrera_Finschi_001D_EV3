from django import forms
from .models import Producto
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'password_confirm']
        widgets = {
            'password': forms.PasswordInput(),
            'password_confirm': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Excluir date_joined del formulario
        self.fields['date_joined'].widget = forms.HiddenInput()
        self.fields['date_joined'].disabled = True  # Opcionalmente, puedes deshabilitar el campo

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password_confirm











class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'imagen', 'precio', 'stock', 'categoria']
        

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        
        
        


        

