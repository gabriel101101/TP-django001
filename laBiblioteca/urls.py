from  django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import  mis_datos, ModificarUsuarioView, EliminarLibroView, ActualizarLibroView, CrearLibroView
from . import views

#CustomLoginView
urlpatterns = [

    path('', views.index, name = 'index'),
    #path("accounts/login/", CustomLoginView.as_view(template_name="laBiblioteca/registration/login.html"), name="login"),
    path('ingresar/', views.ingresar, name='ingresar'),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="laBiblioteca/registration/password_reset.html"), name="password_reset"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    path('catalogo/', views.CatalogoLibros.as_view(), name ='catalogo'),
    path('carrito/agregar/<int:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/quitar/<int:libro_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),
    path('carrito/vaciar', views.clear_cart, name='clear_cart'),
    path('carrito/', views.carrito, name='carrito'),
    path('contactos/', views.contactos, name = 'contactos'),
    path('panel_usuario/', views.panel_usuario, name = 'libros'),
    path('perfil/', views.perfil, name='perfil'),
    path('venta', views.venta, name='venta'),
    path('mis_datos/', mis_datos.as_view(), name='mis_datos'),
    path('modificar_usuario/', ModificarUsuarioView.as_view(), name='modificar_usuario'),

    #==========CRUD============
    path('eliminar_libro/<int:pk>/', EliminarLibroView.as_view(), name='eliminar_libro'),
    path('actualizar_libro/<int:pk>/', ActualizarLibroView.as_view(), name='actualizar_libro'),
    path('crear_libro/', CrearLibroView.as_view(), name='crear_libro'),
    

   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)