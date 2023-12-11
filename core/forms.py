from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Student, User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'city', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name', 'class':'form-control'}),
            'city': forms.TextInput(attrs={'placeholder':'City', 'class':'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone', 'class':'form-control'}),
        }

class RegiserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}),
        #     'email': forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder':'Conf Password', 'class':'form-control'}),
        # }
    