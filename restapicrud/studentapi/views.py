from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from . import serializers
from . import models


class StudentViewset(viewsets.ModelViewSet):

    queryset            =   models.Student.objects.all()
    serializer_class    =   serializers.StudentSerializer



# viewsets internally create few classes:
#     list    -   To get all the values this function will invoke
#     retrive -   To get single function with given id this function will invoke
#     create  -   To create a new record this function will invoke
#     update  -   To update a existing record this function will invoke
#     destroy -   To delete a record this function will invoke