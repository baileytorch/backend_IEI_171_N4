from django.test import TestCase
from django.core.exceptions import ValidationError
from biblioteca.models import validar_rut,validar_mayoria_edad,validar_correo, Nacionalidad, Autor, Comuna
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your tests here.
fecha_actual = date.today()


class TestValidarRut(TestCase):
    def test_rut_valido(self):
        self.assertIsNone(validar_rut('12345678-5'))

    def test_rut_invalido(self):
        with self.assertRaises(ValidationError):
            validar_rut('12345678-4')


class TestValidarEdad(TestCase):
    def test_mayor_edad(self):
        mayor_edad = fecha_actual - relativedelta(years=18)
        self.assertIsNone(validar_mayoria_edad(mayor_edad))

    def test_menor_edad(self):
        menor_edad = fecha_actual - relativedelta(years=17)
        with self.assertRaises(ValidationError):
            validar_mayoria_edad(menor_edad)


class TestValidarCorreo(TestCase):
    def test_correo_valido(self):
        self.assertIsNone(validar_correo('test@test.test'))

    def test_correo_invalido(self):
        with self.assertRaises(ValidationError):
            validar_correo('test@test.')


class TestNacinalidad(TestCase):
    def test_objeto_nacionalidad(self):
        nacionalidad = Nacionalidad.objects.create(
            pais='Chile', nacionalidad='Chileno')

        self.assertEqual(nacionalidad.pais, 'Chile')
        self.assertNotEqual(nacionalidad.pais, 'Argentina')
        self.assertEqual(nacionalidad.nacionalidad, 'Chileno')
        self.assertTrue(Nacionalidad.objects.filter(pais='Chile').exists())
        self.assertFalse(Nacionalidad.objects.filter(pais='Cachiyuyo').exists())

    def test_string_nacionalidad(self):
        nacionalidad = Nacionalidad.objects.create(
            pais='Chile', nacionalidad='Chileno')
        self.assertEqual(str(nacionalidad), 'Chileno')
        self.assertNotEqual(str(nacionalidad), 'Argentino')


class TestAutor(TestCase):
    def test_objeto_autor(self):
        nacionalidad = Nacionalidad.objects.create(
            pais='Chile', nacionalidad='Chileno')
        autor = Autor.objects.create(
            nombre='Ricardo Eliécer Neftalí Reyes Basoalto',
            pseudonimo='Pablo Neruda',
            id_nacionalidad=nacionalidad)

        self.assertEqual(
            autor.nombre, 'Ricardo Eliécer Neftalí Reyes Basoalto')
        self.assertEqual(autor.pseudonimo, 'Pablo Neruda')
        self.assertEqual(autor.id_nacionalidad, nacionalidad)
        self.assertTrue(Autor.objects.filter(
            pseudonimo='Pablo Neruda').exists())

    def test_string_autor(self):
        nacionalidad = Nacionalidad.objects.create(
            pais='Chile', nacionalidad='Chileno')
        autor = Autor.objects.create(
            nombre='Ricardo Eliécer Neftalí Reyes Basoalto',
            pseudonimo='Pablo Neruda',
            id_nacionalidad=nacionalidad)
        self.assertEqual(str(autor), 'Pablo Neruda')


class TestComuna(TestCase):
    def test_objeto_comuna(self):
        comuna = Comuna.objects.create(
            codigo_comuna='09112', nombre_comuna='Padre Las Casas')

        self.assertEqual(comuna.codigo_comuna, '09112')
        self.assertEqual(comuna.nombre_comuna, 'Padre Las Casas')
        self.assertTrue(Comuna.objects.filter(codigo_comuna='09112').exists())

    def test_string_comuna(self):
        comuna = Comuna.objects.create(
            codigo_comuna='09112', nombre_comuna='Padre Las Casas')
        self.assertEqual(str(comuna), 'Padre Las Casas')
