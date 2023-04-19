from django import forms
from Angelaapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'phone_number']


class EmployeeForm(forms.Form):
    firstname = forms.CharField(label="Enter firstname", max_length=50)
    lastname = forms.CharField(label="Enter lastname", max_length=50)
    age = forms.IntegerField(label="Enter age")
    phone = forms.IntegerField(label="Enter phone number")



