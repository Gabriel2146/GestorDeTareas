from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Project, Task
from .forms import EmployeeForm, ProjectForm, TaskForm
from datetime import datetime

def index(request):
    if request.method == 'POST':
        date_start = datetime.strptime(request.POST['date_start'], '%Y-%m-%d').date()
        date_end = datetime.strptime(request.POST['date_end'], '%Y-%m-%d').date()
        tasks = Task.objects.filter(date_start__gte=date_start, date_start__lte=date_end, status="In Progress")
        task_report = []
        for task in tasks:
            task_report.append({
                'task': task,
                'estimated_end': task.date_start + timedelta(days=task.estimate_time),
                'delay': (task.date_start + timedelta(days=task.estimate_time)) - datetime.now().date(),
            })
        return render(request, 'index.html', {'task_report': task_report})

    return render(request, 'index.html')

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('empleados')
    employees = Employee.objects.all()
    form = EmployeeForm()
    return render(request, 'empleados.html', {'employees': employees, 'form': form})

def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('proyectos')
    projects = Project.objects.all()
    form = ProjectForm()
    return render(request, 'proyectos.html', {'projects': projects, 'form': form})

def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tareas')
    tasks = Task.objects.all()
    employees = Employee.objects.all()
    projects = Project.objects.all()
    form = TaskForm()
    return render(request, 'tareas.html', {'tasks': tasks, 'employees': employees, 'projects': projects, 'form': form})

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('empleados')

def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('proyectos')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('tareas')

def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def update_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})
