# Generated by Django 3.2.4 on 2022-12-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_inquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('Unsolved', 'Not Solved')], default='Unsolved', max_length=200, null=True),
        ),
    ]
