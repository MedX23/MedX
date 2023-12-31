# Generated by Django 4.2.5 on 2023-09-21 16:33

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_user_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id_slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='patient_id', unique=True),
        ),
    ]
