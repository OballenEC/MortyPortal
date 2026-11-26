from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from portal.views import home, catalog_view, post_login_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('catalogo/', catalog_view, name='catalog'),
    path('post-login/', post_login_redirect, name='post_login'),
]
