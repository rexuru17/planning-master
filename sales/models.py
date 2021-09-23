from django.db import models
from products.models import Product
from django.urls import reverse


# Create your models here.

class SalesChannel(models.Model):
    code = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    code = models.CharField(max_length=6, primary_key=True, unique=True, help_text="Customer Code 6 digits")
    name = models.CharField(max_length=100, help_text="Customer Name")
    belongs_to_sales_channel = models.ForeignKey(SalesChannel, on_delete=models.RESTRICT, help_text="Select sales channel")
    portfolio = models.ManyToManyField(Product, help_text="Hold Shift to select multiple products or hold Control to select individual products")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sales:customer-detail', kwargs={'pk': self.pk})
    


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

    class Meta:
        unique_together = [['customer', 'date', 'product']]
        # constraints = [
        #     models.UniqueConstraint(fields=['customer', 'date', 'product'], name='unique_salesplan')
        # ]
    
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
        return reverse('sales:sales-plan', kwargs=kwargs)

    def get_absolute_url(self):
        return reverse('sales:sales-plan-detail', kwargs={'pk': self.pk})