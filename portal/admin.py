from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Product, VisualConfig

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Rol en la Plataforma', {'fields': ('role',)}),)
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')
    
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.role == 'ADMIN_CENTRAL'
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.role == 'ADMIN_CENTRAL'
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.role == 'ADMIN_CENTRAL'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')

@admin.register(VisualConfig)
class VisualConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identidad', {'fields': ('platform_name', 'home_title', 'home_subtitle')}),
        ('Colores', {'fields': ('primary_color', 'secondary_color', 'background_color')}),
    )
    def has_add_permission(self, request):
        return not VisualConfig.objects.exists()
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.role in ['ADMIN_CENTRAL', 'ADMIN_DISENO']
