from rest_framework.fields import (
    DateTimeField,
    FloatField,
)
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from sensor_api.fields import StringEnumField
from sensor_api.models import (
    ContinuousSensor,
    ContinuousSensorMeasurement,
)
from sensor_api.unit_definitions import UnitType


class ContinuousSensorSerializer(ModelSerializer):

    _forward_unit_mapping = dict(UnitType.choices)

    _reverse_unit_mapping = {v: k for k, v in UnitType.choices}
    _reverse_unit_mapping.update(
        {"Celcius": UnitType.Celsius}  # Add support for a misspelling, per requirements
    )

    class Meta:
        model = ContinuousSensor
        fields = (
            "id",
            "name",
            "unit",
        )

    unit = StringEnumField(_forward_unit_mapping, _reverse_unit_mapping, source="unit_type")


class ContinuousSensorMeasurementSerializer(ModelSerializer):

    class Meta:
        model = ContinuousSensorMeasurement
        fields = (
            "value",
            "date",
            "sensor",
        )

    value = FloatField(source="unit_converted_value")
    date = DateTimeField(source="time")
    sensor = SlugRelatedField(
        slug_field="name",
        queryset=ContinuousSensor.objects.all()
    )
