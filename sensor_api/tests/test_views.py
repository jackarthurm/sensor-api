from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from sensor_api.models import (
    ContinuousSensor,
    ContinuousSensorMeasurement,
)
from sensor_api.unit_definitions import UnitType


class TestContinuousSensorViewSet(APITestCase):

    def test_create_sensor(self):

        response: Response = self.client.post(
            "/api/sensor",
            data={
                "name": "Main Bearing Temperature",
                "unit": "Celcius"
            },
            format="json"
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        self.assertEqual(
            "Main Bearing Temperature",
            response.data.get("name")
        )
        self.assertEqual(
            "Celsius",
            response.data.get("unit")
        )

    def test_retrieve_sensor(self):

        sensor: ContinuousSensor = ContinuousSensor.objects.create(
            name="Main Bearing Temperature",
            unit_type=UnitType.Celsius
        )

        response: Response = self.client.get(f"/api/sensor/{sensor.id}")

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(
            "Main Bearing Temperature",
            response.data.get("name")
        )
        self.assertEqual(
            "Celsius",
            response.data.get("unit")
        )
        self.assertEqual(
            str(sensor.id),
            response.data.get("id")
        )

    def test_list_sensors(self):

        ContinuousSensor.objects.create(
            name="test sensor 1",
            unit_type=UnitType.Celsius
        )
        ContinuousSensor.objects.create(
            name="test sensor 2",
            unit_type=UnitType.Fahrenheit
        )

        response: Response = self.client.get("/api/sensor/")

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(2, response.data["count"])

        self.assertEqual("test sensor 1", response.data["results"][0]["name"])
        self.assertEqual("Celsius", response.data["results"][0]["unit"])

        self.assertEqual("test sensor 2", response.data["results"][1]["name"])
        self.assertEqual("Fahrenheit", response.data["results"][1]["unit"])


class TestContinuousSensorMeasurementViewSet(APITestCase):

    def test_create_measurement(self):

        ContinuousSensor.objects.create(
            name="Main Bearing Temperature",
            unit_type=UnitType.Celsius
        )

        response: Response = self.client.post(
            "/api/data/",
            data={
                "date": "2022-04-27 12:13",
                "sensor": "Main Bearing Temperature",
                "value": "12.0"
            },
            format="json"
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        self.assertEqual(
            "2022-04-27T12:13:00Z",
            response.data.get("date")
        )
        self.assertEqual(
            12,
            response.data.get("value")
        )
        self.assertEqual(
            "Main Bearing Temperature",
            response.data.get("sensor")
        )

    def test_list_measurements(self):

        sensor_1: ContinuousSensor = ContinuousSensor.objects.create(
            name="test sensor 1",
            unit_type=UnitType.Celsius
        )

        sensor_2: ContinuousSensor = ContinuousSensor.objects.create(
            name="test sensor 2",
            unit_type=UnitType.Celsius
        )

        ContinuousSensorMeasurement.objects.create(sensor=sensor_1, value=42 + 273.15)
        ContinuousSensorMeasurement.objects.create(sensor=sensor_2, value=84 + 273.15)

        response: Response = self.client.get("/api/data/")

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(2, response.data["count"])

        self.assertEqual("test sensor 1", response.data["results"][0]["sensor"])
        self.assertEqual(42, response.data["results"][0]["value"])

        self.assertEqual("test sensor 2", response.data["results"][1]["sensor"])
        self.assertEqual(84, response.data["results"][1]["value"])

    def test_put_request_is_disallowed(self):

        response: Response = self.client.put(
            "/api/data/",
            data={},
            format="json"
        )
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_patch_measurements(self):

        sensor: ContinuousSensor = ContinuousSensor.objects.create(
            name="Main Bearing Temperature",
            unit_type=UnitType.Celsius
        )

        ContinuousSensorMeasurement.objects.create(sensor=sensor, value=42)

        response: Response = self.client.patch(
            "/api/data/",
            data=[
                {
                    "date": "2022-04-27 12:13",
                    "sensor": "Main Bearing Temperature",
                    "value": "12.0"
                },
                {
                    "date": "2023-04-27 12:13",
                    "sensor": "Main Bearing Temperature",
                    "value": 42
                },
            ],
            format="json"
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        self.assertEqual(
            2,
            len(response.data)
        )

        self.assertEqual(
            3,
            ContinuousSensorMeasurement.objects.count()
        )
