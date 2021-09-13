from django import forms
from django.db.models import fields
from .models import *
from django.forms import modelformset_factory

class SalesPlanForm(forms.ModelForm):
    class Meta:
        model = SalesPlan
        fields = '__all__'
        
