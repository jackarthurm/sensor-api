from typing import Mapping

from django.db.models import IntegerChoices

from sensor_api.unit import (
    LinearUnit,
    SIUnit,
    Unit,
)


class UnitType(IntegerChoices):
    Celsius = (1, "Celsius")
    Kelvin = (2, "Kelvin")
    Fahrenheit = (3, "Fahrenheit")
    Hertz = (4, "Hertz")


UNIT_DEFINITIONS: Mapping[UnitType, Unit] = {
    UnitType.Kelvin: SIUnit(),
    UnitType.Celsius: LinearUnit(1, -273.15),
    UnitType.Fahrenheit: LinearUnit(9 / 5, 32 - (9 * 273.15) / 5),
    UnitType.Hertz: SIUnit(),
}
