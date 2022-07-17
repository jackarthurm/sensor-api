from django.test.testcases import SimpleTestCase
from sensor_api.models import (
    ContinuousSensor,
    ContinuousSensorMeasurement,
)
from sensor_api.unit_definitions import UnitType


class TestContinuousSensorMeasurementUnits(SimpleTestCase):

    def test_get_si_value(self):

        sensor: ContinuousSensor = ContinuousSensor(name="test sensor", unit_type=UnitType.Kelvin)
        measurement: ContinuousSensorMeasurement = ContinuousSensorMeasurement(value=0, sensor=sensor)

        self.assertEqual(0, measurement.unit_converted_value)

    def test_get_non_si_value(self):

        sensor: ContinuousSensor = ContinuousSensor(name="test sensor", unit_type=UnitType.Fahrenheit)
        measurement: ContinuousSensorMeasurement = ContinuousSensorMeasurement(value=273.15, sensor=sensor)

        self.assertEqual(32, measurement.unit_converted_value)

    def test_set_si_value(self):

        sensor: ContinuousSensor = ContinuousSensor(name="test sensor", unit_type=UnitType.Kelvin)
        measurement: ContinuousSensorMeasurement = ContinuousSensorMeasurement(value=0, sensor=sensor)

        measurement.unit_converted_value = 32
        self.assertEqual(32, measurement.unit_converted_value)

    def test_set_non_si_value(self):

        sensor: ContinuousSensor = ContinuousSensor(name="test sensor", unit_type=UnitType.Fahrenheit)
        measurement: ContinuousSensorMeasurement = ContinuousSensorMeasurement(value=0, sensor=sensor)

        measurement.unit_converted_value = 32
        self.assertEqual(273.15, measurement.value)
