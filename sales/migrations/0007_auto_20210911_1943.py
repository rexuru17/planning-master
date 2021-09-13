# Generated by Django 3.2.6 on 2021-09-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20210910_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesplan',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesplan',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]