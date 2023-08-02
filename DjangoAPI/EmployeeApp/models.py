from django.db import models

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=90)


class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeesName = models.CharField(max_length=90)
    Department = models.CharField(max_length=90)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=90)

