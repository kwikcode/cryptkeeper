# Generated by Django 3.2.7 on 2021-11-15 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptkeeper', '0017_rename_usd_transaction_fee_transaction_usd_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='quantity',
            new_name='asset_quantity',
        ),
    ]
