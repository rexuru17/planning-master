from django.contrib import admin
from .models import *

# Register your models here.

class CustomerInLine(admin.TabularInline):
    model = Customer
    extra = 0


class SalesChannelAdmin(admin.ModelAdmin):
    inlines = [CustomerInLine]
    list_display = ['name', 'code']




admin.site.register(Customer)
admin.site.register(SalesChannel, SalesChannelAdmin)
admin.site.register(SalesPlan)
admin.site.register(SalesRecords)