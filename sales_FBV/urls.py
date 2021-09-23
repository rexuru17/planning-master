"""planning_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views as sales_views
from .models import *

app_name = 'sales'
urlpatterns = [
    path('create/new/', sales_views.create_sales_plan_redirect, name="create-sales-form"),
    path('create/<str:pk>/<int:year>/<int:month>/<int:day>/', sales_views.create_sales_plan, name='create-sales-plan'),
    path('sales-records/lookup/', sales_views.sales_history_lookup, name='sales-history-lookup'),
    path('sales-records/<str:pk>/<int:year>/<int:month>/<int:day>', sales_views.sales_history, name='sales-history-by-day'),
    path('sales-records/<str:pk>/<int:year>/<int:month>/', sales_views.sales_history, name='sales-history-by-month'),
    path('sales-records/<str:pk>/<int:year>/', sales_views.sales_history, name='sales-history-by-year'),
    path('sales-records/<str:pk>/', sales_views.sales_history, name='sales-history-by-customer'),

]
