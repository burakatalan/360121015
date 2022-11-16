# Generated by Django 4.0 on 2022-11-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movie/images/')),
                ('product_name', models.CharField(max_length=250)),
                ('price', models.FloatField(blank=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('total', models.FloatField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
