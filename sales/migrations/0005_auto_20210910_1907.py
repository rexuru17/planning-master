# Generated by Django 3.2.6 on 2021-09-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20210909_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesplan',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='salesplan',
            name='product',
        ),
        migrations.AddField(
            model_name='salesplan',
            name='product',
            field=models.ManyToManyField(to='sales.SalesPlanItem'),
        ),
    ]