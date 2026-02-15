from django import forms
from .models import AppointmentData

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentData
        fields = '__all__'