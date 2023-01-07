# Generated by Django 3.2.4 on 2022-11-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_producttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productType',
            field=models.CharField(choices=[('Icyayi', 'Tea'), ('Ikawa', 'Coffee'), ('Imyumbati', 'Cassava'), ('Ibijiumba', 'Sweet Potato'), ('Ibirayi', 'Irish Potato'), ('Ibigori', 'Maize'), ('Ibishyimbo', 'Beans')], default='Ibirayi', max_length=200),
        ),
    ]
