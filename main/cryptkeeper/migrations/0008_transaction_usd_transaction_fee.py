# Generated by Django 3.2.7 on 2021-10-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptkeeper', '0007_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='usd_transaction_fee',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
    ]
