# Generated by Django 3.2.7 on 2021-10-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptkeeper', '0008_transaction_usd_transaction_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='usd_transaction_fee',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=True),
        ),
    ]
