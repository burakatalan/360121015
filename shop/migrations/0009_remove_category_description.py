# Generated by Django 4.0 on 2022-12-24 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_newsteller_remove_cart_image_remove_cart_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
