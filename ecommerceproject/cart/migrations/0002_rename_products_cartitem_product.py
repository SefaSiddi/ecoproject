# Generated by Django 4.1.4 on 2023-01-25 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='products',
            new_name='product',
        ),
    ]
