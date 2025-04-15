from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_success')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})