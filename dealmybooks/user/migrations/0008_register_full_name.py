# Generated by Django 4.0.1 on 2022-01-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_register_first_name_remove_register_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='full_name',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]
