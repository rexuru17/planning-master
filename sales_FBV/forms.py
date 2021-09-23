from django import forms
from django.db.models import fields
from .models import *
from django.forms import modelformset_factory, widgets
from django.contrib.humanize.templatetags.humanize import intcomma


class SalesPlanForm(forms.ModelForm):
    product = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = SalesPlan
        fields = '__all__'
        widgets = {
            'customer': forms.HiddenInput(),
            'date': forms.HiddenInput(),
            
        }
        
 
    # def clean_product(self, *args, **kwargs):
    #     cleaned_product = Product.objects.get(id=self.product.id)
    #     return cleaned_product
        

            
    
class SalesPlanFrameForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = SalesPlan
        fields = ('customer', 'date',)


# class SalesRecordsForm(forms.ModelForm):
#     year = forms.IntegerField(min_value=1, max_value=2099, required=False)
#     month = forms.IntegerField(min_value=1, max_value=12, required=False)
#     day = forms.IntegerField(min_value=1, max_value=31, required=False)

#     class Meta:
#         model = SalesRecords
#         fields = ('customer',)