from django import forms
from .models import Student, Result

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "roll", "subject", "phone", "address")

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ("marks", "grade", "total_marks")
