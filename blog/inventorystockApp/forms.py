from django import forms
from .models import inventorystockdata

class inventorystockdataForm(forms.ModelForm):
    class Meta:
        model = inventorystockdata
        fields = '__all__'