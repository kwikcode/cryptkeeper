# Generated by Django 3.2.7 on 2021-12-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptkeeper', '0023_transaction_needs_reviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='spot_price',
            field=models.DecimalField(decimal_places=10, max_digits=19, null=True),
        ),
    ]
