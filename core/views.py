from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Project, Task
from .forms import EmployeeForm, ProjectForm, TaskForm
from datetime import datetime, timedelta  # Asegúrate de importar timedelta

# Vista principal para generar el reporte de tareas
def index(request):
    tasks = []
    date_start = None
    date_end = None

    if request.method == 'POST':
        # Obtener las fechas de inicio y fin desde el formulario
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')

        # Convertir las fechas de string a datetime
        try:
            if date_start:
                date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
            if date_end:
                date_end = datetime.strptime(date_end, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse('Fecha no válida', status=400)

        # Depuración: Imprimir las fechas para asegurarse de que se están recibiendo correctamente
        print(f"Fecha de inicio: {date_start}")
        print(f"Fecha de fin: {date_end}")

        # Obtener las tareas dentro del rango de fechas y con estado "En Progreso"
        tasks = Task.objects.filter(date_start__gte=date_start, date_start__lte=date_end, status="En Progreso")

        # Depuración: Imprimir las tareas obtenidas
        print(f"Tareas obtenidas: {tasks}")

        # Calcular las fechas estimadas de finalización y el retraso de cada tarea
        for task in tasks:
            # Calcula la fecha estimada de finalización
            estimated_end_date = task.date_start + timedelta(days=task.estimate_time)
            # Calcula el retraso (si hay alguno)
            delay = (datetime.today().date() - estimated_end_date).days
            # Agregar estos valores como atributos dinámicos
            task.estimated_end_date = estimated_end_date
            task.delay = delay

    # Mostrar las tareas en el contexto
    return render(request, 'index.html', {
        'tasks': tasks,
        'date_start': date_start,
        'date_end': date_end
    })


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
    employees = Employee.objects.all()  # Asegúrate de pasar los empleados
    projects = Project.objects.all()  # Asegúrate de pasar los proyectos

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TaskForm()

    return render(request, 'tareas.html', {
        'tasks': tasks,
        'form': form,
        'employees': employees,  # Pasar empleados al template
        'projects': projects,  # Pasar proyectos al template
    })


# Vista para editar tarea
def editar_tarea(request, id):
    task = get_object_or_404(Task, id=id)
    employees = Employee.objects.all()  # Pasar empleados disponibles para la tarea
    projects = Project.objects.all()  # Pasar proyectos disponibles para la tarea

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {
        'form': form,
        'task': task,
        'employees': employees,  # Pasar empleados al template
        'projects': projects,  # Pasar proyectos al template
    })


# Vista para eliminar tarea
def eliminar_tarea(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tareas')
