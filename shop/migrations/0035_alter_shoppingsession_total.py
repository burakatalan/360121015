# Generated by Django 4.0 on 2023-01-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_cart_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingsession',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
