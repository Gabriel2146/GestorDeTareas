from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados/', views.empleados, name='empleados'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('tareas/', views.tareas, name='tareas'),
    path('editar_empleado/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('editar_proyecto/<int:id>/', views.editar_proyecto, name='editar_proyecto'),
    path('editar_tarea/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar_empleado/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('eliminar_proyecto/<int:id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('eliminar_tarea/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
]

