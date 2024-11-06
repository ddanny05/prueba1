from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_lista, name='producto_lista'),
    path('crear/', views.producto_crear, name='producto_crear'),
    path('editar/<int:id>/', views.producto_editar, name='producto_editar'),
    path('eliminar/<int:id>/', views.producto_eliminar, name='producto_eliminar'),
]
