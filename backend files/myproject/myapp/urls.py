from django.urls import path
from . import views
from .views import home
from .views import obtener_todos_usuarios


urlpatterns = [
    path('', views.home, name="home"),
    path('api/usuarios', views.obtener_todos_usuarios),
]


