# Generated by Django 3.2.7 on 2021-11-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptkeeper', '0018_rename_quantity_transaction_asset_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='notes',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Sell', 'Sell'), ('Interest', 'Interest'), ('Send', 'Send'), ('Airdrop', 'Airdrop'), ('Receive', 'Receive')], max_length=40),
        ),
    ]
