# Generated by Django 3.2.4 on 2022-11-12 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_producttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='demo_link',
        ),
        migrations.RemoveField(
            model_name='product',
            name='source_link',
        ),
    ]
