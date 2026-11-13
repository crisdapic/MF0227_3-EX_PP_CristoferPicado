
from django.test import TestCase
from django.urls import reverse

from .models import Tecnico, Incidencia
from .forms import IncidenciaForm


class TecnicoModelTest(TestCase):

    def setUp(self):
        self.tecnico = Tecnico.objects.create(
            nombre="Carlos Pérez",
            especialidad="Informática",
            email="carlos@example.com"
        )

    def test_creacion_tecnico(self):
        self.assertEqual(self.tecnico.nombre, "Carlos Pérez")
        self.assertEqual(self.tecnico.especialidad, "Informática")
        self.assertEqual(str(self.tecnico), "Carlos Pérez (Informática)")


class IncidenciaModelTest(TestCase):

    def setUp(self):
        self.tecnico = Tecnico.objects.create(
            nombre="Ana López",
            especialidad="Redes",
            email="ana@example.com"
        )

        self.incidencia = Incidencia.objects.create(
            titulo="Error de conexión",
            descripcion="No hay conexión a Internet",
            prioridad="ALTA",
            tecnico=self.tecnico
        )

    def test_creacion_incidencia(self):
        self.assertEqual(self.incidencia.titulo, "Error de conexión")
        self.assertEqual(self.incidencia.estado, "ABIERTO")
        self.assertEqual(self.incidencia.prioridad, "ALTA")

    def test_asignacion_tecnico(self):
        self.assertEqual(self.incidencia.tecnico, self.tecnico)

    def test_fecha_creacion(self):
        self.assertIsNotNone(self.incidencia.fecha_creacion)

    def test_representacion_incidencia(self):
        self.assertEqual(
            str(self.incidencia),
            "[Abierto] Error de conexión"
        )


class IncidenciaFormTest(TestCase):

    def test_formulario_valido(self):
        form = IncidenciaForm(data={
            "titulo": "Equipo averiado",
            "descripcion": "El ordenador no arranca",
            "estado": "ABIERTO",
            "prioridad": "MEDIA"
        })

        self.assertTrue(form.is_valid())

    def test_titulo_obligatorio(self):
        form = IncidenciaForm(data={
            "titulo": "",
            "descripcion": "Descripción de prueba",
            "estado": "ABIERTO",
            "prioridad": "MEDIA"
        })

        self.assertFalse(form.is_valid())
        self.assertIn("titulo", form.errors)
