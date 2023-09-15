# Generated by Django 4.2.4 on 2023-09-02 16:59

import app.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_user_profile'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', app.models.manager.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='profile/'),
        ),
    ]