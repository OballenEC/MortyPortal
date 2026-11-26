from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    return render(request, 'portal/home.html')

@login_required
def catalog_view(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'portal/catalog.html', {'products': products})

@login_required
def post_login_redirect(request):
    """Redirige según el rol del usuario tras iniciar sesión."""
    if request.user.is_staff:
        return redirect('admin:index')
    return redirect('catalog')
