# Generated by Django 4.2.5 on 2023-09-21 11:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_appointment_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='email', unique=True),
        ),
    ]
