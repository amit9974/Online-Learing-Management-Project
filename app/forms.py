from .models import Student
from django.forms import forms

class StudentRegisterForm(forms.Form):
    class Meta:

        model = Student
        fields = "__all__"


        
