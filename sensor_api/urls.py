from django.urls import path
from django.views import View
from rest_framework.routers import SimpleRouter

from sensor_api.views import (
    ContinuousSensorViewSet,
    ContinuousSensorMeasurementView,
)

router = SimpleRouter()
router.register("sensor", ContinuousSensorViewSet)

# Provide a set of URLs without a trailing slash, per requirements
no_slash_router = SimpleRouter(trailing_slash=False)
no_slash_router.register("sensor", ContinuousSensorViewSet)

measurement_view: View = ContinuousSensorMeasurementView.as_view()

urlpatterns = [
    path("data/", measurement_view),
    path("data", measurement_view),
] + router.urls + no_slash_router.urls
