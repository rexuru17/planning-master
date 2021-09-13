from django.db import models
from products.models import Product


# Create your models here.

class SalesChannel(models.Model):
    code = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class Customer(models.Model):
    code = models.CharField(max_length=6, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    belongs_to_sales_channel = models.ForeignKey(SalesChannel, on_delete=models.RESTRICT)
    portfolio = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class SalesPlanItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.FloatField()

# class CustomerPortfolio(models.Model):
#     customer = 
#     product = 
        

class SalesRecords(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    date = models.DateField()
    quantity = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    
class SalesPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    date = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        sales_plan_info = str(self.customer) + ' - ' + str(self.date) + ' - ' + str(self.product)
        return str(sales_plan_info)