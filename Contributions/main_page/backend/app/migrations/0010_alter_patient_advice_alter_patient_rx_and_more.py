# Generated by Django 4.2.5 on 2023-09-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_medicine_patient_advice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='advice',
            field=models.TextField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rx',
            field=models.TextField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='suggestion_test',
            field=models.TextField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.TextField(default='NULL'),
        ),
    ]
