from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    ROLE_CHOICES = [
        ('external', 'External User'),
        ('internal', 'Internal User'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']


from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['serial_number', 'product_name', 'date_of_purchase', 'fault_description', 'photo']
        widgets = {
            'date_of_purchase': forms.DateInput(attrs={'type': 'date'}),
        }       
        
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']        