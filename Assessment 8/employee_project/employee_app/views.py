from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

# Create
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_app/employee_form.html', {'form': form})

# Read
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', {'employees': employees})

# Update
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_app/employee_form.html', {'form': form})

# Delete
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_app/employee_confirm_delete.html', {'employee': employee})

