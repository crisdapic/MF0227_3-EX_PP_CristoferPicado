from django.db import models

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Técnico")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"


class Incidencia(models.Model):
    ESTADO_CHOICES = [
        ('ABIERTO', 'Abierto'),
        ('EN_PROCESO', 'En Proceso'),
        ('CERRADO', 'Cerrado'),
    ]

    PRIORIDAD_CHOICES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]

    titulo = models.CharField(max_length=150, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ABIERTO', verbose_name="Estado")
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='MEDIA', verbose_name="Prioridad")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencias', verbose_name="Técnico Asignado")

    def __str__(self):
        return f"[{self.get_estado_display()}] {self.titulo}"

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ['-fecha_creacion']