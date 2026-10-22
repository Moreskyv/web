from django import forms
from .models import Groups, Student, Grade


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'group']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'value']