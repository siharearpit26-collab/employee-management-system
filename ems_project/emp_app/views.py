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
    departments = Department.objects.all()
    roles = Role.objects.all()
    context = {'departments': departments, 'roles': roles, 'success': False, 'error': None}

    if request.method == 'POST':
        try:
            Employee.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                department=Department.objects.get(id=request.POST['department']),
                role=Role.objects.get(id=request.POST['role']),
                salary=request.POST['salary'],
                bonus=request.POST.get('bonus', 0),
                phone=request.POST['phone'],
                hire_date=request.POST['hire_date'],
            )
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)

    return render(request, 'add-emp.html', context)

def remove_employee(request, employee_id):
    context = {'success': False, 'error': None, 'employee': None}

    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            context['success'] = True
        except Employee.DoesNotExist:
            context['error'] = f"No employee found with ID {emp_id}."
        except Exception as e:
            context['error'] = str(e)
    elif employee_id != 1:
        # pre-fill if a real ID was passed in the URL
        try:
            context['employee'] = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            pass

    return render(request, 'remove-emp.html', context)

def filter_employee(request, employee_id):
    departments = Department.objects.all()
    roles = Role.objects.all()
    emps = None
    filtered = False

    if request.method == 'GET' and any(request.GET.values()):
        filtered = True
        emps = Employee.objects.all()
        first_name = request.GET.get('first_name', '').strip()
        last_name = request.GET.get('last_name', '').strip()
        department = request.GET.get('department', '').strip()
        role = request.GET.get('role', '').strip()
        hire_date = request.GET.get('hire_date', '').strip()

        if first_name:
            emps = emps.filter(first_name__icontains=first_name)
        if last_name:
            emps = emps.filter(last_name__icontains=last_name)
        if department:
            emps = emps.filter(department__id=department)
        if role:
            emps = emps.filter(role__id=role)
        if hire_date:
            emps = emps.filter(hire_date=hire_date)

    context = {
        'departments': departments,
        'roles': roles,
        'emps': emps,
        'filtered': filtered,
        'get': request.GET,
    }
    return render(request, 'filter-emp.html', context)