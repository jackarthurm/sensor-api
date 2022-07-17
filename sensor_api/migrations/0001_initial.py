# Generated by Django 4.0.6 on 2022-07-17 15:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContinuousSensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='sensor name')),
                ('unit_type', models.PositiveSmallIntegerField(choices=[(1, 'Celsius'), (2, 'Kelvin'), (3, 'Fahrenheit')], verbose_name='measurement unit')),
            ],
            options={
                'verbose_name': 'continuous sensor',
                'verbose_name_plural': 'continuous sensors',
            },
        ),
        migrations.CreateModel(
            name='ContinuousSensorMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='sensor_api.continuoussensor')),
            ],
            options={
                'verbose_name': 'continuous sensor measurement',
                'verbose_name_plural': 'continuous sensor measurements',
            },
        ),
    ]