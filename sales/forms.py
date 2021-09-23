from django import forms
from django.db.models import fields
from .models import *
from django.forms import modelformset_factory, widgets
from django.contrib.humanize.templatetags.humanize import intcomma


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            
        }


class SalesPlanForm(forms.ModelForm):
    # product = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = SalesPlan
        fields = '__all__'
        widgets = {
            'customer': forms.HiddenInput(),
            'date': forms.HiddenInput(),
            
        }

SalesPlanFormSet = modelformset_factory(SalesPlan, form=SalesPlanForm, extra=0)
    
class SalesPlanFrameForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = SalesPlan
        fields = ('customer', 'date',)

