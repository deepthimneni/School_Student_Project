from django import forms
from students.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        widgets = { 
            'address': forms.Textarea(),
        } 
        fields = "__all__"