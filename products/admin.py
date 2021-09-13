from django.contrib import admin
from .models import *

# Register your models here.


class ProductInLine(admin.TabularInline):
    model = Product
    fields = ['product_group', 'product_subgroup', 'code', 'name']
    extra = 0


admin.site.register(Product)

class ProductSubGroupInLine(admin.TabularInline):
    model = ProductSubGroup
    fields = ['product_subgroup']
    extra = 0

class ProductGroupAdmin(admin.ModelAdmin):
    inlines = [ProductSubGroupInLine, ProductInLine]
    list_display = ['product_group']


admin.site.register(ProductGroup, ProductGroupAdmin)


admin.site.register(ProductSubGroup)
# admin.site.register(ProductCategory)

