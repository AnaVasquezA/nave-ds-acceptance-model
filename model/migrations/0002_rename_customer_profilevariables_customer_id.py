# Generated by Django 4.0.1 on 2022-07-08 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilevariables',
            old_name='customer',
            new_name='customer_id',
        ),
    ]
