# Generated by Django 4.0.1 on 2022-01-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='username',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='register',
            name='last_name',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]
