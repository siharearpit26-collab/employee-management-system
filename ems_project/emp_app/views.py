from django.shortcuts import render
from .models import Employee, Department, Role, Attendance
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_employee(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view-all-emp.html', context)

def add_employee(request):
    return render(request, 'add-emp.html')

def remove_employee(request, employee_id):
    return render(request, 'remove-emp.html')

def filter_employee(request, employee_id):
    return render(request, 'filter-emp.html')                