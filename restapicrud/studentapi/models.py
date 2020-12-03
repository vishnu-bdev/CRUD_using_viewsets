from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lasstname = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)

    class Meta:
        db_table = 'students'

    # C - Create / Insert / Add - POST
    # R - Retrive / Fetch       - GET
    # U - Update / Edit         - PUT
    # D - Delete / Remove       - DELETE
