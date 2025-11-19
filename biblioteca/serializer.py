from rest_framework import serializers
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo


class NacionalidadSerializer(serializers.ModelSerializer):
    pais = serializers.CharField(max_length=50, label='País')
    nacionalidad = serializers.CharField(max_length=50, label='Nacionalidad')

    class Meta:
        model = Nacionalidad
        fields = [
            'pais',
            'nacionalidad',
        ]


class AutorSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=250, label='Nombre')
    pseudonimo = serializers.CharField(max_length=50, label='Pesudónimo')
    biografia = serializers.CharField(label='Biografía')

    nacionalidad = serializers.StringRelatedField(
        source='id_nacionalidad', read_only=True)
    id_nacionalidad = serializers.PrimaryKeyRelatedField(
        queryset=Nacionalidad.objects.all()
    )

    class Meta:
        model = Autor
        fields = [
            'id',
            'nombre',
            'pseudonimo',
            'biografia',
            'id_nacionalidad',
            'nacionalidad',
        ]


class ComunaSerializer(serializers.ModelSerializer):
    codigo_comuna = serializers.CharField(max_length=5, label='Código')
    nombre_comuna = serializers.CharField(max_length=50, label='Nombre')

    class Meta:
        model = Comuna
        fields = [
            'id',
            'codigo_comuna',
            'nombre_comuna',
        ]


class DireccionSerializer(serializers.ModelSerializer):
    calle = serializers.CharField(label='Calle', max_length=50)
    numero = serializers.CharField(label='Número', max_length=10)
    departamento = serializers.CharField(
        label='Departamento', max_length=10)
    detalles = serializers.CharField(label='Detalles')

    comuna = serializers.StringRelatedField(
        source='id_comuna', read_only=True)
    id_comuna = serializers.PrimaryKeyRelatedField(
        queryset=Comuna.objects.all()
    )

    class Meta:
        model = Direccion
        fields = [
            'id',
            'calle',
            'numero',
            'departamento',
            'detalles',
            'id_comuna',
            'comuna',
        ]


class BibliotecaSerializer(serializers.ModelSerializer):
    nombre_biblioteca = serializers.CharField(max_length=100, label='Nombre')
    web = serializers.CharField(max_length=255, label='Página WEB')

    class Meta:
        model = Biblioteca
        fields = [
            'id',
            'nombre_biblioteca',
            'web',
        ]


class LectorSerializer(serializers.ModelSerializer):
    rut_lector = serializers.CharField(label='RUT')
    nombre_lector = serializers.CharField(max_length=255, label='Nombre')
    correo_lector = serializers.CharField(max_length=255, label='Email')
    fecha_nacimiento = serializers.DateField(label='Fecha Nacimiento')

    biblioteca = serializers.StringRelatedField(
        source='id_biblioteca', read_only=True)
    id_biblioteca = serializers.PrimaryKeyRelatedField(
        queryset=Biblioteca.objects.all()
    )

    direccion = serializers.StringRelatedField(
        source='id_direccion', read_only=True)
    id_direccion = serializers.PrimaryKeyRelatedField(
        queryset=Direccion.objects.all()
    )

    class Meta:
        model = Lector
        fields = [
            'id',
            'rut_lector',
            'nombre_lector',
            'correo_lector',
            'fecha_nacimiento',
            'id_biblioteca',
            'biblioteca',
            'id_direccion',
            'direccion',
        ]


class TipoCategoriaSerializer(serializers.ModelSerializer):
    tipo_categoria = serializers.CharField(
        max_length=50, label='Tipo Categoría')

    class Meta:
        model = TipoCategoria
        fields = [
            'id',
            'tipo_categoria',
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(max_length=100, label='Categoría')
    descripcion = serializers.CharField(max_length=255, label='Descripción')

    tipo_categoria = serializers.StringRelatedField(
        source='id_tipo_categoria', read_only=True)
    id_tipo_categoria = serializers.PrimaryKeyRelatedField(
        queryset=TipoCategoria.objects.all()
    )

    class Meta:
        model = Categoria
        fields = [
            'id',
            'categoria',
            'descripcion',
            'id_tipo_categoria',
            'tipo_categoria',
        ]


class LibroSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(max_length=255, label='Título')
    paginas = serializers.IntegerField(label='Páginas')
    copias = serializers.IntegerField(label='Copias')
    ubicacion = serializers.CharField(max_length=255, label='Ubicación')
    fisico = serializers.BooleanField(label='¿Es libro físico?')

    biblioteca = serializers.StringRelatedField(
        source='id_biblioteca', read_only=True)
    id_biblioteca = serializers.PrimaryKeyRelatedField(
        queryset=Biblioteca.objects.all()
    )

    categoria = serializers.StringRelatedField(
        source='id_categoria', read_only=True)
    id_categoria = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all()
    )

    autor = serializers.StringRelatedField(
        source='id_autor', read_only=True)
    id_autor = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all()
    )

    class Meta:
        model = Libro
        fields = [
            'id',
            'titulo',
            'paginas',
            'copias',
            'ubicacion',
            'fisico',
            'id_biblioteca',
            'biblioteca',
            'id_categoria',
            'categoria',
            'id_autor',
            'autor',
        ]


class PrestamoSerializer(serializers.ModelSerializer):
    fecha_prestamo = serializers.DateTimeField(label='Fecha Préstamo')
    fecha_devolucion = serializers.DateField(label='Fecha Devolución')
    fecha_retorno = serializers.DateTimeField(label='Fecha Retorno')

    libro = serializers.StringRelatedField(
        source='id_libro', read_only=True)
    id_libro = serializers.PrimaryKeyRelatedField(
        queryset=Libro.objects.all()
    )

    lector = serializers.StringRelatedField(
        source='id_lector', read_only=True)
    id_lector = serializers.PrimaryKeyRelatedField(
        queryset=Lector.objects.all()
    )

    class Meta:
        model = Prestamo
        fields = [
            'id',
            'fecha_prestamo',
            'fecha_devolucion',
            'fecha_retorno',
            'id_libro',
            'libro',
            'id_lector',
            'lector',
        ]
