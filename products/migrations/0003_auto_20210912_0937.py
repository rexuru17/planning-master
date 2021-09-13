# Generated by Django 3.2.6 on 2021-09-12 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210909_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='item_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_group',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='item_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_subgroup',
            new_name='subgroup',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_weight',
            new_name='weight',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_weight_text',
            new_name='weight_text',
        ),
        migrations.RenameField(
            model_name='productgroup',
            old_name='product_group',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='productsubgroup',
            old_name='product_group',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='productsubgroup',
            old_name='product_subgroup',
            new_name='subgroup',
        ),
    ]