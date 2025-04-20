from django.db import models
from datetime import timedelta

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_start = models.DateField()
    estimate_time = models.IntegerField()  # Tiempo estimado en días
    status = models.CharField(max_length=50)

    def estimated_end(self):
        # Método para calcular la fecha estimada de finalización
        return self.date_start + timedelta(days=self.estimate_time)

    def __str__(self):
        return self.description
