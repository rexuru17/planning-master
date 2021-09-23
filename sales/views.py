from django.shortcuts import redirect, render, get_object_or_404
from django.forms import formset_factory, formsets, modelformset_factory
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import *
from .forms import *
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.db.models import Sum, F
import pandas as pd


# Customer Views #
#########################################################


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    
    # def get_success_url(self):
    #     return reverse('sales:customer-detail', kwargs={'pk': self.object.pk})


class CustomerDetailView(DetailView):
    model = Customer
    

class CustomerListView(ListView):
    model = Customer
    ordering = ['belongs_to_sales_channel', 'code',]


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('sales:customer-list')
    
    
class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('sales:customer-list')


# Sales Plan Views #
#########################################################

def create_sales_plan_redirect(request, pk=None, year=None, month=None, day=None):
    form = SalesPlanFrameForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        return redirect(obj.get_creation_url())
    context = {
        'form': form
    }
    return render(request, 'sales/salesplan_form.html', context)

def create_sales_plan(request, pk, year, month, day):
    customer = get_object_or_404(Customer, code=pk)
    portfolio = customer.portfolio.all()
    date = str(str(year)+'-'+str(month)+'-'+str(day))
    initial = []
    for item in portfolio:
        initial.append({'customer':customer, 'product':item, 'quantity':0, 'date':date})
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
        'customer': customer,
        'date': date,
    }
    return render(request, 'sales/salesplan-create.html', context)


class SalesPlanListView(ListView):
    """
    Should consider changing to function based view to make it more palatable and functional:
    for example, introduce filter for customers, dates and display plans below in the table.
    Also, nice thing would be to be able to delete all plans for customer and date selected.
    """
    model = SalesPlan
    ordering = ['date', 'customer', 'product',]


class SalesPlanDetailView(DetailView):
    model = SalesPlan
    

class SalesPlanUpdateView(UpdateView):
    model = SalesPlan
    fields = '__all__'
    success_url = reverse_lazy('sales:sales-plan-list')


class SalesPlanDeleteView(DeleteView):
    model = SalesPlan
    success_url = reverse_lazy('sales:sales-plan-list')