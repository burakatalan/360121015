# Generated by Django 4.0 on 2023-01-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_cart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='productImg/'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_homr',
            field=models.BooleanField(default=False),
        ),
    ]
