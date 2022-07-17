# Generated by Django 4.0.6 on 2022-07-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='continuoussensor',
            options={'ordering': ('name',), 'verbose_name': 'continuous sensor', 'verbose_name_plural': 'continuous sensors'},
        ),
        migrations.AlterModelOptions(
            name='continuoussensormeasurement',
            options={'ordering': ('time',), 'verbose_name': 'continuous sensor measurement', 'verbose_name_plural': 'continuous sensor measurements'},
        ),
        migrations.AlterField(
            model_name='continuoussensor',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='continuoussensor',
            name='unit_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Celsius'), (2, 'Kelvin'), (3, 'Fahrenheit'), (4, 'Hertz')], verbose_name='measurement unit'),
        ),
    ]