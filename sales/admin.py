from django.contrib import admin
from .models import *

# Register your models here.

class CustomerInLine(admin.TabularInline):
    model = Customer
    extra = 0

admin.site.register(Customer)

class SalesChannelAdmin(admin.ModelAdmin):
    inlines = [CustomerInLine]
    list_display = ['name', 'code']

admin.site.register(SalesChannel, SalesChannelAdmin)
admin.site.register(SalesPlanItem)
admin.site.register(SalesPlan)