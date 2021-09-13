from django.shortcuts import render
from products.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.
class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('')
