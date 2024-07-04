/*
 
<div class="card m-5" style="width: 18rem;">
                
                <img src="{{ libro.portada }}" alt="Portada del libro">
                <div class="card-body">
                    <h5 class="card-title">ISBN: {{ libro.isbn }}</h5>
                    <p>Título: {{ libro.titulo }}</p>
                    <p>Autor: {{ libro.autor }}</p>
                    <p>Precio: {{ libro.precio }}</p>
                    <p>Stock: {{ libro.stock }}</p>
                    <a class="btn btn-primary" href="{% url 'agregar_al_carrito' libro.id %}">AGREGAR</a>
                </div>
            </div>



            <form class="container-fluid pb-2 form" action="{% url 'ingresar' %}" method="post">
            {% csrf_token %}
            <div class="d-flex flex-column mb-2">
                {{ ingreso_lector_form.email.label_tag }}
                {{ ingreso_lector_form.email }}
                {{ ingreso_lector_form.email.errors }}
            </div>
          
            <div class="d-flex flex-column mb-4">
                {{ ingreso_lector_form.contrasenia.label_tag }}
                {{ ingreso_lector_form.contrasenia }}
                {{ ingreso_lector_form.contrasenia.errors }}
            </div>
            <div class="mb-0 d-flex justify-content-center">
                <input class="btn btn-primary mb-1 py-2 w-50" type="submit" value="INGRESAR">
            </div>
        </form>






        <form class="container-fluid pb-2 form" action="{% url 'perfil' %}" method="post">
            {% csrf_token %}
            <div class="d-flex flex-column mb-2">
                {{ perfil_form.nombre.label_tag }}
                {{ perfil_form.nombre }}
                {{ perfil_form.nombre.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ perfil_form.apellido.label_tag }}
                {{ perfil_form.apellido }}
                {{ perfil_form.apellido.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ perfil_form.email.label_tag }}
                {{ perfil_form.email }}
                {{ perfil_form.email.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ perfil_form.contrasenia.label_tag }}
                {{ perfil_form.contrasenia }}
                {{ perfil_form.contrasenia.errors }}
                <span class="helptext">{{ perfil_form.contrasenia.help_text }}</span>
            </div>
            <div class="d-flex flex-column mb-4">
                {{ perfil_form.descripcion.label_tag }}
                {{ perfil_form.descripcion }}
                {{ perfil_form.descripcion.errors }}
            </div>
            <div class="mb-0 d-flex justify-content-center">
                <input class="btn btn-primary mb-1 py-2 w-50" type="submit" value="ENVIAR">
            </div>
        </form>
*/





















/*

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            self.add_error('password2', "Las contraseñas deben ser iguales")

        return cleaned_data

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.set_password(self.cleaned_data["password"])

        #tabla auth_user
        user = User.objects.create_user(
            username=cliente.usuario,
            email=cliente.email,
            password=self.cleaned_data["password"],
            first_name=cliente.nombre,
            last_name=cliente.apellido
        )

        if commit:
            cliente.save()
        return cliente
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not re.match(r'^[a-zA-Z\s]+$', nombre):
            raise ValidationError("El nombre solo puede estar compuesto por letras y espacios")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get("apellido")
        if not re.match(r'^[a-zA-Z\s]+$', apellido):
            raise ValidationError("El apellido solo puede estar compuesto por letras y espacios")
        return apellido

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        contraseña = cleaned_data.get("contraseña")
        contraseña2 = cleaned_data.get("repetirContraseña")

        if not contraseña == contraseña2:
            raise ValidationError("Las contraseñas deben ser iguales")

        return self.cleaned_data    


*/

























/*
        
            <div class="d-flex flex-column mb-2">
                {{ alta_lector_form.usuario.label_tag }}
                {{ alta_lector_form.usuario }}
                {{ alta_lector_form.usuario.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ alta_lector_form.nombre.label_tag }}
                {{ alta_lector_form.nombre }}
                {{ alta_lector_form.nombre.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ alta_lector_form.apellido.label_tag }}
                {{ alta_lector_form.apellido }}
                {{ alta_lector_form.apellido.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ alta_lector_form.dni.label_tag }}
                {{ alta_lector_form.dni }}
                {{ alta_lector_form.dni.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ alta_lector_form.email.label_tag }}
                {{ alta_lector_form.email }}
                {{ alta_lector_form.email.errors }}
            </div>
            <div class="d-flex flex-column mb-2">
                {{ alta_lector_form.password.label_tag }}
                {{ alta_lector_form.password }}
                {{ alta_lector_form.password.errors }}
                <span class="helptext">{{ alta_lector_form.password.help_text }}</span>
            </div>
            <div class="d-flex flex-column mb-4">
                {{ alta_lector_form.password2.label_tag }}
                {{ alta_lector_form.password2 }}
                {{ alta_lector_form.password2.errors }}
            </div>
            <div class="d-flex flex-column mb-4">
                {{ alta_lector_form.direccion.label_tag }}
                {{ alta_lector_form.direccion }}
                {{ alta_lector_form.direccion.errors }}
            </div>

            <div class="mb-0 d-flex justify-content-center">
                <input class="btn btn-primary mb-1 py-2 w-50" type="submit" value="REGISTRARSE">
            </div>
            
        
 */