# Generated by Django 3.2.6 on 2021-09-10 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210909_1959'),
        ('sales', '0005_auto_20210910_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesplan',
            name='quantity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='salesplan',
            name='product',
        ),
        migrations.AddField(
            model_name='salesplan',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.RESTRICT, to='products.product'),
            preserve_default=False,
        ),
    ]