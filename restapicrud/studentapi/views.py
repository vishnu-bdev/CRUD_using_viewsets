# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from . import serializers
# from . import models


# class StudentViewset(viewsets.ModelViewSet):

#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer



# viewsets internally create few classes:
#     list    -   To get all the values this function will invoke
#     retrive -   To get single function with given id this function will invoke
#     create  -   To create a new record this function will invoke
#     update  -   To update a existing record this function will invoke
#     destroy -   To delete a record this function will invoke

def index(request):
    return render(request, '../templates/index.html')


from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
