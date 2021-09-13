from django.shortcuts import render
from sales.models import *
from products.models import *
from sales.forms import *


# Create your views here.
def home_view(request):
    sales_channels = SalesChannel.objects.all()
    customers = Customer.objects.all()
    products = Product.objects.all()
    context = {
        'sales_channels': sales_channels,
        'products': products,
        'customers': customers,
    }
    return render(request, 'dashboard/home.html', context)

