from django import views
from django.urls import path
from .views import GuitarraDelete, InstrumentoCreacion, GuitarraDetalle, AmplificadorLista, TecladoLista, BateriaLista, BajoLista, GuitarraLista, PedalLista, OtroLista, BajoDetalle, PedalDetalle, AmplificadorDetalle, TecladoDetalle, BateriaDetalle, OtroDetalle, GuitarraUpdate, BajoUpdate, PedalUpdate, AmplificadorUpdate, TecladoUpdate, BateriaUpdate, OtroUpdate, BajoDelete, PedalDelete, AmplificadorDelete, TecladoDelete, BateriaDelete, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', views.inicio, name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaGuitarras/', GuitarraLista.as_view(), name='guitarras'),
    path('listaBajos/', BajoLista.as_view(), name='bajos'),
    path('listaPedales/', PedalLista.as_view(), name='pedales'),
    path('listaBaterias/', BateriaLista.as_view(), name='baterias'),
    path('listaTeclados/', TecladoLista.as_view(), name='teclados'),
    path('listaAmplificadores/', AmplificadorLista.as_view(), name='amplificadores'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('guitarraDetalle/<int:pk>/', GuitarraDetalle.as_view(), name='guitarra'),
    path('bajoDetalle/<int:pk>/', BajoDetalle.as_view(), name='bajo'),
    path('pedalDetalle/<int:pk>/', PedalDetalle.as_view(), name='pedal'),
    path('amplificadorDetalle/<int:pk>/', AmplificadorDetalle.as_view(), name='amplificador'),
    path('tecladoDetalle/<int:pk>/', TecladoDetalle.as_view(), name='teclado'),
    path('bateriaDetalle/<int:pk>/', BateriaDetalle.as_view(), name='bateria'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('guitarraEdicion/<int:pk>/', GuitarraUpdate.as_view(), name='guitarra_editar'),
    path('bajoEdicion/<int:pk>/', BajoUpdate.as_view(), name='bajo_editar'),
    path('pedalEdicion/<int:pk>/', PedalUpdate.as_view(), name='pedal_editar'),
    path('amplificadorEdicion/<int:pk>/', AmplificadorUpdate.as_view(), name='amplificador_editar'),
    path('tecladoEdicion/<int:pk>/', TecladoUpdate.as_view(), name='teclado_editar'),
    path('bateriaEdicion/<int:pk>/', BateriaUpdate.as_view(), name='bateria_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),


    path('guitarraBorrado/<int:pk>/', GuitarraDelete.as_view(), name='guitarra_eliminar'),
    path('bajoBorrado/<int:pk>/', BajoDelete.as_view(), name='bajo_eliminar'),
    path('pedalBorrado/<int:pk>/', PedalDelete.as_view(), name='pedal_eliminar'),
    path('amplificadorBorrado/<int:pk>/', AmplificadorDelete.as_view(), name='amplificador_eliminar'),
    path('tecladoBorrado/<int:pk>/', TecladoDelete.as_view(), name='teclado_eliminar'),
    path('bateriaBorrado/<int:pk>/', BateriaDelete.as_view(), name='bateria_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('instrumentoCreacion/', InstrumentoCreacion.as_view(), name='nuevo'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]
