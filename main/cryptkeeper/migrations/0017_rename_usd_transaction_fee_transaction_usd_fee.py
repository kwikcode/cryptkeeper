# Generated by Django 3.2.7 on 2021-11-15 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptkeeper', '0016_rename_usd_price_transaction_spot_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='usd_transaction_fee',
            new_name='usd_fee',
        ),
    ]
