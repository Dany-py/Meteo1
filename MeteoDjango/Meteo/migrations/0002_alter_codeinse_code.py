# Generated by Django 5.0.2 on 2024-08-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meteo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeinse',
            name='code',
            field=models.IntegerField(),
        ),
    ]
