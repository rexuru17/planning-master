# Generated by Django 3.2.6 on 2021-09-20 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20210912_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salesrecords',
            options={'verbose_name_plural': 'Sales Records'},
        ),
        migrations.DeleteModel(
            name='SalesPlanItem',
        ),
    ]
