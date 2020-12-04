# from django.db import models

# # Create your models here.
# class Student(models.Model):
#     firstname = models.CharField(max_length=100)
#     lasstname = models.CharField(max_length=100)
#     roll_no = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'students'

    # C - Create / Insert / Add - POST
    # R - Retrive / Fetch       - GET
    # U - Update / Edit         - PUT
    # D - Delete / Remove       - DELETE

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = '__all__'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    class Meta:
        db_table = '__all__'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    
    class Meta:
        db_table = '__all__'


