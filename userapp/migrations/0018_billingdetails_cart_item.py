# Generated by Django 5.0.2 on 2024-03-27 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0017_remove_cartitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='cart_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_details', to='userapp.cartitem'),
        ),
    ]