#here we dine the fields for our table like we have an employee table

from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=30,null=True) 
    home_district = models.CharField(max_length=30,blank=True) 
    salary = models.FloatField( null=True)
    

    def __str__(self):
        return self.ename
