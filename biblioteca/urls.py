from django.urls import path, include
from rest_framework import routers
from biblioteca import views

router = routers.DefaultRouter()

router.register(r'nacionalidades', views.Nacionalidad_ViewSet)
router.register(r'autores', views.Autor_ViewSet)
router.register(r'comunas', views.Comuna_ViewSet)
router.register(r'direcciones', views.Direccion_ViewSet)
router.register(r'bibliotecas', views.Biblioteca_ViewSet)
router.register(r'lectores', views.Lector_ViewSet)
router.register(r'tipos_categorias', views.TipoCategoria_ViewSet)
router.register(r'categorias', views.Categoria_ViewSet)
router.register(r'libros', views.Libro_ViewSet)
router.register(r'prestamos', views.Prestamo_ViewSet)

urlpatterns = [
    path('', include(router.urls))
]
