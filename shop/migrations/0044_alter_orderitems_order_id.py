# Generated by Django 4.0 on 2023-01-29 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_alter_orderitems_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.orders'),
        ),
    ]
