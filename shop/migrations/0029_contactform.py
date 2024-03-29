# Generated by Django 4.0 on 2023-01-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_product_sold_count_product_top_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
