from django.contrib.admin import site

from sensor_api.models import (
    ContinuousSensor,
    ContinuousSensorMeasurement,
)

site.register(ContinuousSensor)
site.register(ContinuousSensorMeasurement)
