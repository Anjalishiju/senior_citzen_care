# Generated by Django 5.0.2 on 2024-03-19 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_rename_total_price_cartitem_original_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='original_price',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='image',
        ),
    ]