from django.db import models

# Create your models here.


class ProductGroup(models.Model):
    product_group = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.product_group


class ProductSubGroup(models.Model):
    product_group = models.ForeignKey(ProductGroup, on_delete=models.RESTRICT)
    product_subgroup = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.product_subgroup


class Product(models.Model):
    product_group = models.ForeignKey(ProductGroup, on_delete=models.RESTRICT)
    product_subgroup = models.ForeignKey(ProductSubGroup, on_delete=models.RESTRICT)
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    weight_text = models.CharField(max_length=10)

    def __str__(self):
        product_info = str(self.code) + ' - ' + str(self.name)
        return str(product_info)
