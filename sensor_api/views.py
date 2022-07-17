from typing import List, Dict

from django_filters import CharFilter
from django_filters.rest_framework import FilterSet
from rest_framework import status
from rest_framework.generics import GenericAPIView
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


class ContinuousSensorFilterSet(FilterSet):
    sensor = CharFilter(field_name="sensor__name", lookup_expr='iexact')


class ContinuousSensorMeasurementView(ListModelMixin, GenericAPIView):

    queryset = ContinuousSensorMeasurement.objects.all()
    serializer_class = ContinuousSensorMeasurementSerializer
    filterset_class = ContinuousSensorFilterSet

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def patch(self, request: Request) -> Response:

        bulk_data: List[Dict] = request.data.get("bulk_data", [])

        sz = self.get_serializer(data=bulk_data, many=True)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={"bulk_data": sz.data}
        )

    def post(self, request: Request) -> Response:

        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(status=status.HTTP_201_CREATED, data=sz.data)
