from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import django_filters

from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView, DetailView  # Vistas para VER
from django.views.generic import CreateView, UpdateView, DeleteView  # Vistas para EDITAR
from django.views.generic import View, TemplateView, RedirectView  # Vistas BÁSICAS
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin, UserPassesTestMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .serializer import NacionalidadSerializer, AutorSerializer, ComunaSerializer, DireccionSerializer, BibliotecaSerializer, LibroSerializer, TipoCategoriaSerializer, CategoriaSerializer, LectorSerializer, PrestamoSerializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo
from .forms import NacionalidadForm

# Create your views here.


def logout_view(request):
    # Cierra la sesión del usuario y limpia la data de SESSION
    logout(request)
    # Redirige a la página de inicio de sesión
    return redirect('login')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def pagina_inicio(request):
    # Almacenar data en SESSION
    request.session['mensaje_bienvenida'] = '¡Bienvenido!'
    # Obtener data desde SESSION
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')
    # Remover data desde SESSION
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']
    return render(request, 'biblioteca/inicio.html', {'message': mensaje_bienvenida})

class NacionalidadListView(PermissionRequiredMixin, ListView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    permission_required = ('biblioteca.view_nacionalidad')
    model = Nacionalidad
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

class NacionalidadCreateView(PermissionRequiredMixin, CreateView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    permission_required = ('biblioteca.add_nacionalidad')
    model = Nacionalidad
    form_class = NacionalidadForm

class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer


class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer


class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer


class TipoCategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroFilter(django_filters.FilterSet):
    id_biblioteca = django_filters.ModelChoiceFilter(queryset=Biblioteca.objects.all(),label='Biblioteca')
    id_categoria = django_filters.ModelChoiceFilter(queryset=Categoria.objects.all(),label='Categoría')
    id_autor = django_filters.ModelChoiceFilter(queryset=Autor.objects.all(),label='Autor')
    class Meta:
        model = Libro
        fields = ['id_biblioteca','id_categoria','id_autor']

@login_required
def listado_libros(request):
    permisos = request.user.user_permissions.all()
    f = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(request, 'biblioteca/lista_libros.html',{'filtro': f,'permisos':permisos})


class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
