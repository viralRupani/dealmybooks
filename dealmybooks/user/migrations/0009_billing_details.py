# Generated by Django 4.0.1 on 2022-01-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_register_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(max_length=10)),
                ('street_address', models.CharField(max_length=200)),
                ('apartment_address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('postcode', models.BigIntegerField(max_length=15)),
            ],
        ),
    ]