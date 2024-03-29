# Generated by Django 4.0 on 2022-11-18 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_subcategory_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useradress',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.user'),
            preserve_default=False,
        ),
    ]
