from django.shortcuts import redirect, render
from django.forms import formset_factory, modelformset_factory
from .models import *
from .forms import *
from django.views.generic import CreateView

# Create your views here.
class SalesPlanFormView(CreateView):
    model = SalesPlan
    fields = ['customer', 'product', 'quantity']

    def get_initial(self):
        initial = super().get_initial()
        initial['customer'] = Customer.objects.first()
  
        return initial
    success_url = ''

def create_sales_plan(request, pk):
    customer = Customer.objects.get(code=pk)
    portfolio = customer.portfolio.all()
    initial = []
    for item in portfolio:
        initial.append({'customer': customer, 'product':item, 'quantity': 0})
    SalesPlanFormSet = formset_factory(SalesPlanForm, extra=0)
    formset = SalesPlanFormSet(initial=initial)
    if request.method == "POST":
        formset = SalesPlanFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                quantity = form.cleaned_data['quantity']
                if quantity > 0 :
                    form.save()
            return redirect('/')
    context = {
        'formset': formset,
    }
    return render(request, 'sales/salesplan-create.html', context)