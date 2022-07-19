from django_filters import CharFilter
from django_filters.rest_framework import FilterSet
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from sensor_api.models import (
    ContinuousSensor,
    ContinuousSensorMeasurement,
)
from sensor_api.serializers import (
    ContinuousSensorSerializer,
    ContinuousSensorMeasurementSerializer,
)


class ContinuousSensorViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    queryset = ContinuousSensor.objects.all()
    serializer_class = ContinuousSensorSerializer


class ContinuousSensorMeasurementFilterSet(FilterSet):
    sensor = CharFilter(field_name="sensor__name", lookup_expr="iexact")


class ContinuousSensorMeasurementView(ListAPIView, CreateAPIView):

    queryset = ContinuousSensorMeasurement.objects.all()
    serializer_class = ContinuousSensorMeasurementSerializer
    filterset_class = ContinuousSensorMeasurementFilterSet

    def patch(self, request: Request) -> Response:
        """Creates a list of sensor measurement resources"""

        sz = self.get_serializer(data=request.data, many=True)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data=sz.data
        )
