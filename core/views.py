from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Project, Task
from .forms import EmployeeForm, ProjectForm, TaskForm
from datetime import datetime

# Vista principal para generar el reporte de tareas
def index(request):
    tasks = []
    if request.method == 'POST':
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')

        # Convertir las fechas de string a datetime
        try:
            date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
            date_end = datetime.strptime(date_end, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse('Fecha no válida', status=400)

        # Obtener las tareas dentro del rango de fechas y en progreso
        tasks = Task.objects.filter(date_start__gte=date_start, date_start__lte=date_end, status="In Progress")

        # Calcular las fechas estimadas de finalización y el retraso de cada tarea
        for task in tasks:
            task.estimated_end_date = task.date_start + timedelta(days=task.estimate_time)
            task.delay = (datetime.today().date() - task.estimated_end_date).days

    return render(request, 'index.html', {'tasks': tasks})


# Vista para manejar empleados
def empleados(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmployeeForm()

    return render(request, 'empleados.html', {
        'employees': employees,
        'form': form
    })


# Vista para editar empleado
def editar_empleado(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})


# Vista para eliminar empleado
def eliminar_empleado(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('empleados')


# Vista para manejar proyectos
def proyectos(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProjectForm()

    return render(request, 'proyectos.html', {
        'projects': projects,
        'form': form
    })


# Vista para editar proyecto
def editar_proyecto(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})


# Vista para eliminar proyecto
def eliminar_proyecto(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('proyectos')


# Vista para manejar tareas
def tareas(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TaskForm()

    return render(request, 'tareas.html', {
        'tasks': tasks,
        'form': form
    })


# Vista para editar tarea
def editar_tarea(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


# Vista para eliminar tarea
def eliminar_tarea(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tareas')
