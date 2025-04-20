from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('empleados/', views.employee, name='empleados'),
    path('proyectos/', views.project, name='proyectos'),
    path('tareas/', views.task, name='tareas'),

    path('eliminar_empleado/<int:id>/', views.delete_employee, name='eliminar_empleado'),
    path('eliminar_proyecto/<int:id>/', views.delete_project, name='eliminar_proyecto'),
    path('eliminar_tarea/<int:id>/', views.delete_task, name='eliminar_tarea'),

    path('editar_empleado/<int:id>/', views.update_employee, name='editar_empleado'),
    path('editar_proyecto/<int:id>/', views.update_project, name='editar_proyecto'),
    path('editar_tarea/<int:id>/', views.update_task, name='editar_tarea'),
]
