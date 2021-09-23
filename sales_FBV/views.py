from django.shortcuts import redirect, render, get_object_or_404
from django.forms import formset_factory, modelformset_factory
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.db.models import Sum, F
import pandas as pd
# Create your views here.
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

def sales_history_lookup(request, pk=None, year=None, month=None, day=None):
    customer = Customer.objects.all()
    year = None
    month = None
    day = None
    if request.method == "POST":
        print(request.POST)
    """
    Need to find a way to pass the query
    """
    context = {
       'customer': customer,
       'year': year,
       'month': month,
       'day': day, 
    }
    return render(request, 'sales/salesplan_form.html', context)

def sales_history(request, year=None, month=None, day=None, pk=None):
    customer = get_object_or_404(Customer, code=pk)
    """
    Need to update query regarding periods to exclude dumb data like year = 2 and then total is None...
    """
    year = year
    month = month
    if year:
        if month:
            if day:
                customer_history = SalesRecords.objects.filter(customer=customer, date__year=year, date__month=month, date__day=day)
            else:
                customer_history = SalesRecords.objects.filter(customer=customer, date__year=year, date__month=month)
        else:
            customer_history = SalesRecords.objects.filter(customer=customer, date__year=year)
    else:
        customer_history = SalesRecords.objects.filter(customer=customer)
    total_sales = customer_history.aggregate(Sum('quantity'))
    group_sales = customer_history.values(product_group=F('product__product_group__product_group')).annotate(quantity=Sum('quantity'))
    total_sales = total_sales['quantity__sum']
    group_sales = pd.DataFrame(group_sales)
    group_sales = group_sales.to_html()

    """
    Here I need to make pivot data for all product groups to display totals per group.
    """
    # pgroups = {}
    # pgs = ProductGroup.objects.all()
    # for pg in pgs:
    #     totals = customer_history.filter(product__product_group__product_group=pg).aggregate(Sum('quantity'))
    #     pgroups  ['product_line'] = pg
    #     pgroups['total_sales'] = totals['quantity__sum']
    context = {
        'total_sales': total_sales,
        'customer_history': customer_history,
        'group_sales': group_sales,
    }
    return render(request, 'sales/sales-records.html', context)