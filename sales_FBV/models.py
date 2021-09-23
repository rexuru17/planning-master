from django.db import models
from products.models import Product
from django.urls import reverse


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


class SalesRecords(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    date = models.DateField()
    quantity = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)

    class Meta:
        verbose_name_plural = "Sales Records"

    def __str__(self):
        sales_records_info = str(self.customer) + ' - ' + str(self.date) + ' - ' + str(self.product)
        return str(sales_records_info)
    
   
  
    
class SalesPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    date = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        sales_plan_info = str(self.customer) + ' - ' + str(self.date) + ' - ' + str(self.product)
        return str(sales_plan_info)

    def get_creation_url(self):
        kwargs={
            'pk': str(self.customer.code),
            'year': str(self.date.year),
            'month': str(self.date.month),
            'day': str(self.date.day)
        }
        return reverse('sales:create-sales-plan', kwargs=kwargs)