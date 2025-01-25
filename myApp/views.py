from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, ResultForm



#CRUD OPERATIONS
def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        result_form = ResultForm(request.POST)

        if student_form.is_valid() and result_form.is_valid():
            student = student_form.save()
            result = result_form.save(commit=False)
            result.student = student
            result.save()
            return redirect("student_list")  # Replace with your URL name for the student list
    else:
        student_form = StudentForm()
        result_form = ResultForm()
    return render(
        request,
        "add_student.html",
        {"student_form": student_form, "result_form": result_form},
    )



# Create updated  student informantion
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    result = student.results.first()

    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        result_form = ResultForm(request.POST, instance=result)

        if student_form.is_valid() and result_form.is_valid():
            student_form.save()
            result_form.save()
            return redirect("student_list")  # Replace with your URL name for the student list  
    else:
        student_form = StudentForm(instance=student)
        result_form = ResultForm(instance=result)
    return render(
        request,
        "student_update.html",
        {"student": student, "student_form": student_form, "result_form": result_form},
    )


# Delete student information

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    result = student.results.first()
    student.delete()
    return redirect("student_list")  # Replace with your URL name for the student list
