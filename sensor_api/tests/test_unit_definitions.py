from unittest import TestCase

from sensor_api.unit import Unit
from sensor_api.unit_definitions import (
    UNIT_DEFINITIONS,
    UnitType,
)


class TestCelsius(TestCase):

    def test_from_si(self) -> None:

        celsius: Unit = UNIT_DEFINITIONS[UnitType.Celsius]

        self.assertEqual(
            0,
            celsius.from_si(273.15)
        )

    def test_to_si(self) -> None:

        celsius: Unit = UNIT_DEFINITIONS[UnitType.Celsius]

        self.assertEqual(
            273.15,
            celsius.to_si(0)
        )


class TestFahrenheit(TestCase):

    def test_from_si(self) -> None:

        fahrenheit: Unit = UNIT_DEFINITIONS[UnitType.Fahrenheit]

        self.assertEqual(
            32,
            fahrenheit.from_si(273.15)
        )

    def test_to_si(self) -> None:

        fahrenheit: Unit = UNIT_DEFINITIONS[UnitType.Fahrenheit]

        self.assertEqual(
            273.15,
            fahrenheit.to_si(32)
        )
