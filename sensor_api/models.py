from datetime import datetime
from typing import Optional
from uuid import (
    UUID,
    uuid4,
)

from django.db.models import (
    Model,
    DateTimeField,
    UUIDField,
    CharField,
    FloatField,
    PositiveSmallIntegerField,
    ForeignKey,
    CASCADE,
    Manager,
)
from django.utils.timezone import now

from sensor_api.unit import Unit
from sensor_api.unit_definitions import (
    UnitType,
    UNIT_DEFINITIONS,
)


class ContinuousSensor(Model):
    """Represents a physical sensor resource which
    records measurements of a continuous quantity
    over a period of time
    """

    class Meta:
        verbose_name = "continuous sensor"
        verbose_name_plural = "continuous sensors"
        ordering = ("name",)

    objects: Manager
    _meta: Meta

    id: UUID = UUIDField(primary_key=True, default=uuid4, editable=False)
    name: Optional[str] = CharField(max_length=256, unique=True)
    unit_type: Optional[UnitType] = PositiveSmallIntegerField(
        verbose_name="measurement unit",
        choices=UnitType.choices
    )

    @property
    def unit(self) -> Optional[Unit]:

        if self.unit_type is None:
            return None

        try:
            return UNIT_DEFINITIONS[self.unit_type]
        except KeyError:
            raise RuntimeError(
                f"Missing unit definition for unit type {self.unit_type.name}"
            )

    def __str__(self) -> str:
        return str(self.name)


class ContinuousMeasurement(Model):
    """Abstract model representing a continuous measurement
    recorded at a given point in time
    """

    class Meta:
        abstract = True

    value: Optional[float] = FloatField()
    time: datetime = DateTimeField(default=now)

    def __str__(self) -> str:
        return f"{self.value:.5g} @ {self.time}"


class ContinuousSensorMeasurement(ContinuousMeasurement):
    """Model representing a continuous measurement
    recorded by a given sensor at a given point in time
    """

    class Meta:
        verbose_name = "continuous sensor measurement"
        verbose_name_plural = "continuous sensor measurements"
        ordering = ("time",)

    objects: Manager
    _meta: Meta

    sensor: Optional[ContinuousSensor] = ForeignKey(
        to=ContinuousSensor,
        on_delete=CASCADE,
        related_name="measurements"
    )

    @property
    def unit_converted_value(self) -> Optional[float]:

        return None if self.value is None else float(
            self.sensor.unit.from_si(self.value)
        )

    @unit_converted_value.setter
    def unit_converted_value(self, value: Optional[float]) -> None:

        self.value = None if value is None else float(
            self.sensor.unit.to_si(value)
        )
