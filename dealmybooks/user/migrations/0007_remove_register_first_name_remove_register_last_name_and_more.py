# Generated by Django 4.0.1 on 2022-01-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_username_register_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
