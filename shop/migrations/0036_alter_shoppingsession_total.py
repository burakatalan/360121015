# Generated by Django 4.0 on 2023-01-14 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_alter_shoppingsession_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingsession',
            name='total',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
