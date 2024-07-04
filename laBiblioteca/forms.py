from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from .models import Cliente, User, Libro, Mensaje
import re
from .models import Libro

class AltaLectoresForm(UserCreationForm):
    password2 = forms.CharField(label="Repita su Contraseña", widget=forms.PasswordInput, required=True)

    class Meta:
        model = Cliente
        fields = ['usuario', 'nombre', 'apellido', 'dni', 'email', 'password', 'password2', 'direccion']
        widgets = {
            'password': forms.PasswordInput(),
        }


    def clean_dni(self):
        dni = str(self.cleaned_data['dni'])  # Convertir a cadena antes de validar
        # Ejemplo de validación básica de DNI: asegurar que sea un número válido
        if not dni.isdigit():
            raise forms.ValidationError("El DNI debe contener solo números.")
        return dni

    def clean_email(self):
        email = self.cleaned_data['email']
        # Validación de email: asegurar que el email sea único en la base de datos
        if Cliente.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # Validación de las contraseñas: asegurar que coincidan
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        # Validación de la fortaleza de la contraseña
        password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.dni = self.cleaned_data['dni']
        user.direccion = self.cleaned_data['direccion']
        if commit:
            user.save()
        return user


##=============================================================================
##=============================================================================
##=============================================================================
class IngresoLectoresForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    contraseña = forms.CharField(label="Contraseña", required=True)

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = '__all__'
        widgets = {
            'mensaje': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class PerfilForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    apellido = forms.CharField(max_length=50, label="Apellido", required=True)
    email = forms.EmailField(label="Email", required=True)
    contrasenia = forms.CharField(min_length=8, max_length=162, label="Contraseña", required=True, 
                                  widget=forms.PasswordInput, 
                                  help_text="Mínimo 8 caracteres, con al menos una letra minúscula, una letra \
                                             mayúscula y un número.")
    descripcion = forms.CharField(max_length=255, label="Descripción", required=False)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if not nombre.isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras.")

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')

        if not apellido.isalpha():
            raise forms.ValidationError("El apellido solo debe contener letras.")

        return apellido

    """def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya se encuentra registrado.")

        return email"""

    def clean_contrasenia(self):
        re_contrasenia = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{,}$"
        contrasenia = self.cleaned_data.get('contrasenia')

        if not re.match(re_contrasenia, contrasenia):
            raise forms.ValidationError("La contraseña no es válida.")

        return contrasenia
    
    
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'portada', 'titulo', 'autor', 'precio', 'stock']
        
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class UsuarioStaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

#Creando formulario personalizado
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'precio', 'isbn', 'portada', 'stock']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio
    
