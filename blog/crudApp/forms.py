from django import forms
from .models import ExpenseTracker

class ExpenseTrackerForm(forms.ModelForm):
    class Meta:
        model = ExpenseTracker
        fields = '__all__'