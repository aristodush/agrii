# Generated by Django 3.2.4 on 2022-12-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20221113_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
