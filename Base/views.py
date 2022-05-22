from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Instrumento, Avatar
from .forms import ActualizacionInstrumento, FormularioEdicion, FormularioNuevoInstrumento, FormularioRegistroUsuario


# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = 'Base/home.html'

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(usuario=request.user.id)
    imagenAvatar = avatares[0].imagenAvatar.url
    return render(request, "base/home.html", {'url': imagenAvatar})

class LoginPagina(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'base/registro.html'
    #form_class = UserCreationForm
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'base/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'base/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'base/passwordExitoso.html', {})


# GUITARRA

class GuitarraLista(LoginRequiredMixin, ListView):
    context_object_name = 'guitarras'
    queryset = Instrumento.objects.filter(instrumento__startswith='guitarra')
    template_name = 'Base/listaGuitarras.html'
    login_url = '/login/'

class GuitarraDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'guitarra'
    template_name = 'Base/guitarraDetalle.html'

class GuitarraUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'Base/guitarraEdicion.html'

class GuitarraDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'Base/guitarraBorrado.html'

# BAJO

class BajoLista(LoginRequiredMixin, ListView):
    context_object_name = 'bajos'
    queryset = Instrumento.objects.filter(instrumento__startswith='bajo')
    template_name = 'Base/listaBajos.html'

class BajoDetalle(LoginRequiredMixin,DetailView):
    model = Instrumento
    context_object_name = 'bajo'
    template_name = 'Base/bajoDetalle.html'

class BajoUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('bajos')
    context_object_name = 'bajo'
    template_name = 'Base/bajoEdicion.html'

class BajoDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('bajos')
    context_object_name = 'bajo'
    template_name = 'Base/bajoBorrado.html'

# PEDAL

class PedalLista(LoginRequiredMixin, ListView):
    context_object_name = 'pedales'
    queryset = Instrumento.objects.filter(instrumento__startswith='pedal')
    template_name = 'Base/listaPedales.html'

class PedalDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'pedal'
    template_name = 'Base/pedalDetalle.html'

class PedalUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('pedales')
    context_object_name = 'pedal'
    template_name = 'Base/pedalEdicion.html'

class PedalDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('pedales')
    context_object_name = 'pedal'
    template_name = 'Base/pedalBorrado.html'

# AMPLIFICADOR

class AmplificadorLista(LoginRequiredMixin, ListView):
    context_object_name = 'amplificadores'
    queryset = Instrumento.objects.filter(instrumento__startswith='amplificador')
    template_name = 'Base/listaAmplificadores.html'

class AmplificadorDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'amplificador'
    template_name = 'Base/amplificadorDetalle.html'

class AmplificadorUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('amplificadores')
    context_object_name = 'amplificador'
    template_name = 'Base/amplificadorEdicion.html'

class AmplificadorDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('amplificadores')
    context_object_name = 'amplificador'
    template_name = 'Base/amplificadorBorrado.html'

# TECLADO

class TecladoLista(LoginRequiredMixin, ListView):
    context_object_name = 'teclados'
    queryset = Instrumento.objects.filter(instrumento__startswith='teclado')
    template_name = 'Base/listaTeclados.html'

class TecladoDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'teclado'
    template_name = 'Base/tecladoDetalle.html'

class TecladoUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'Base/tecladoEdicion.html'

class TecladoDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'Base/tecladoBorrado.html'

# BATERIA

class BateriaLista(LoginRequiredMixin, ListView):
    context_object_name = 'baterias'
    queryset = Instrumento.objects.filter(instrumento__startswith='bateria')
    template_name = 'Base/listaBaterias.html'

class BateriaDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'bateria'
    template_name = 'Base/bateriaDetalle.html'

class BateriaUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('baterias')
    context_object_name = 'bateria'
    template_name = 'Base/bateriaEdicion.html'

class BateriaDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('baterias')
    context_object_name = 'bateria'
    template_name = 'Base/bateriaBorrado.html'


# OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Instrumento.objects.filter(instrumento__startswith='otro')
    template_name = 'Base/listaOtros.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'otro'
    template_name = 'Base/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroBorrado.html'

# CREACION INSTRUMENTO

class InstrumentoCreacion(LoginRequiredMixin, CreateView):
    model = Instrumento
    form_class = FormularioNuevoInstrumento
    success_url = reverse_lazy('home')
    template_name = 'Base/instrumentoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InstrumentoCreacion, self).form_valid(form)


# ACERCA DE MI

def about(request):
    return render(request, 'base/acercaDeMi.html', {})


