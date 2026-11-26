from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN_CENTRAL', 'Administrador Central'),
        ('ADMIN_CATALOGO', 'Administrador de Catálogo'),
        ('ADMIN_DISENO', 'Administrador de Diseño'),
        ('CLIENTE', 'Cliente'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CLIENTE', verbose_name="Rol en la Plataforma")

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción")
    is_active = models.BooleanField(default=True, verbose_name="Activa")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoría")
    name = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    description = models.TextField(blank=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class VisualConfig(models.Model):
    platform_name = models.CharField(max_length=100, default="Morty's Portal", verbose_name="Nombre de la Plataforma")
    primary_color = models.CharField(max_length=7, default="#97CE4C", verbose_name="Color Primario (Hex)")
    secondary_color = models.CharField(max_length=7, default="#8A2BE2", verbose_name="Color Secundario (Hex)")

    class Meta:
        verbose_name = "Configuración Visual"
        verbose_name_plural = "Configuración Visual"

    def __str__(self):
        return "Ajustes de Apariencia"
