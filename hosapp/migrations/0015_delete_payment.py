# Generated by Django 5.0.2 on 2024-03-27 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0014_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]