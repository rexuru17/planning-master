from django.urls import path
from . import views as sales_views
from .models import *

app_name = 'sales'
urlpatterns = [
    path('customer/new/', sales_views.CustomerCreateView.as_view(), name="customer-create"),
    path('customer/list/', sales_views.CustomerListView.as_view(), name="customer-list"),
    path('customer/update/<int:pk>/', sales_views.CustomerUpdateView.as_view(), name="customer-update"),
    path('customer/detail/<int:pk>/', sales_views.CustomerDetailView.as_view(), name="customer-detail"),
    path('customer/delete/<int:pk>/', sales_views.CustomerDeleteView.as_view(), name="customer-delete"),
    path('plan/new/', sales_views.create_sales_plan_redirect, name='sales-plan-create-form'),
    path('plan/new/<str:pk>/<int:year>/<int:month>/<int:day>/', sales_views.create_sales_plan, name="sales-plan"),
    path('plan/list/', sales_views.SalesPlanListView.as_view(), name="sales-plan-list"),
    path('plan/detail/<int:pk>', sales_views.SalesPlanDetailView.as_view(), name="sales-plan-detail"),
    path('plan/update/<int:pk>/', sales_views.SalesPlanUpdateView.as_view(), name="sales-plan-update"),
    path('plan/delete/<int:pk>/', sales_views.SalesPlanDeleteView.as_view(), name="sales-plan-delete"),

]
