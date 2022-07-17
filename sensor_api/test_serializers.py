from datetime import datetime

from django.test import TestCase
from django.utils import timezone
from rest_framework.exceptions import ErrorDetail

from sensor_api.models import ContinuousSensor, ContinuousSensorMeasurement
from sensor_api.serializers import ContinuousSensorSerializer, ContinuousSensorMeasurementSerializer
from sensor_api.unit_definitions import UnitType


class TestContinuousSensorSerializer(TestCase):

    def test_create_sensor(self):

        sensor_sz: ContinuousSensorSerializer = ContinuousSensorSerializer(
            data={
                "name": "test sensor name",
                "unit": "Celsius"
            }
        )
        sensor_sz.is_valid()
        instance: ContinuousSensor = sensor_sz.save()

        self.assertEqual("test sensor name", instance.name)
        self.assertEqual(UnitType.Celsius, instance.unit_type)

    def test_create_sensor_supports_celcius_misspelling(self):

        sensor_sz: ContinuousSensorSerializer = ContinuousSensorSerializer(
            data={
                "name": "test sensor name",
                "unit": "Celcius"
            }
        )
        sensor_sz.is_valid()
        instance: ContinuousSensor = sensor_sz.save()

        self.assertEqual("test sensor name", instance.name)
        self.assertEqual(UnitType.Celsius, instance.unit_type)

    def test_create_sensor_duplicate_name_is_invalid(self):

        ContinuousSensor.objects.create(name="test sensor name", unit_type=UnitType.Kelvin)

        sensor_sz: ContinuousSensorSerializer = ContinuousSensorSerializer(
            data={
                "name": "test sensor name",
                "unit": "Celsius"
            }
        )

        is_valid: bool = sensor_sz.is_valid()
        self.assertFalse(False, is_valid)

        error_detail: ErrorDetail = sensor_sz.errors["name"][0]

        self.assertEqual(
            "continuous sensor with this sensor name already exists.",
            str(error_detail)
        )

    def test_create_sensor_name_too_long(self):

        sensor_sz: ContinuousSensorSerializer = ContinuousSensorSerializer(
            data={
                "name": "x" * 257,
                "unit": "Celsius"
            }
        )

        is_valid: bool = sensor_sz.is_valid()
        self.assertFalse(False, is_valid)

        error_detail: ErrorDetail = sensor_sz.errors["name"][0]

        self.assertEqual(
            "Ensure this field has no more than 256 characters.",
            str(error_detail)
        )


class TestContinuousSensorMeasurementSerializer(TestCase):

    def test_create_sensor_measurement(self):

        sensor: ContinuousSensor = ContinuousSensor.objects.create(
            name="test sensor name",
            unit_type=UnitType.Kelvin
        )

        measurement_sz: ContinuousSensorMeasurementSerializer = ContinuousSensorMeasurementSerializer(
            data={
                "value": 12,
                "date": "2022-12-1 11:22",
                "sensor": "test sensor name"
            }
        )
        measurement_sz.is_valid()
        instance: ContinuousSensorMeasurement = measurement_sz.save()

        self.assertEqual(12, instance.value)
        self.assertEqual(
            datetime(year=2022, month=12, day=1, hour=11, minute=22, tzinfo=timezone.utc),
            instance.time
        )
        self.assertEqual(sensor.id, instance.sensor.id)
