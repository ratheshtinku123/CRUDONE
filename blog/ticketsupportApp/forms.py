from .models import TicketTracker
from django import forms

class TicketTrackerForm(forms.ModelForm):
    class Meta:
        model = TicketTracker
        fields = '__all__'