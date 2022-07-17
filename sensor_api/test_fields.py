from enum import Enum

from django.test.testcases import SimpleTestCase
from rest_framework.exceptions import ValidationError

from sensor_api.fields import StringEnumField


class TestStringEnumField(SimpleTestCase):

    def test_to_representation_valid(self):

        class ExampleEnum(Enum):
            First = 1
            Second = 2

        field = StringEnumField(
            {ExampleEnum.First: "one", ExampleEnum.Second: "two"},
            {},
        )

        self.assertEqual(
            "one",
            field.to_representation(ExampleEnum.First)
        )
        self.assertEqual(
            "two",
            field.to_representation(ExampleEnum.Second)
        )

    def test_to_representation_invalid(self):

        class ExampleEnum(Enum):
            First = 1
            Second = 2

        field: StringEnumField = StringEnumField(
            {ExampleEnum.First: "one"},
            {},
        )

        self.assertIsNone(
            field.to_representation(ExampleEnum.Second)
        )

    def test_to_internal_value_valid(self):

        class ExampleEnum(Enum):
            First = 1
            Second = 2

        field = StringEnumField(
            {},
            {"one": ExampleEnum.First, "two": ExampleEnum.Second},
        )

        self.assertEqual(
            ExampleEnum.First,
            field.to_internal_value("one")
        )
        self.assertEqual(
            ExampleEnum.Second,
            field.to_internal_value("two")
        )

    def test_to_internal_value_invalid(self):

        class ExampleEnum(Enum):
            First = 1
            Second = 2

        field = StringEnumField(
            {ExampleEnum.First: "one"},
            {},
        )

        with self.assertRaises(ValidationError) as ex:
            field.to_internal_value("two")

        self.assertListEqual(
            ['"two" does not map to an enum value.'],
            ex.exception.detail
        )

    def test_to_internal_value_case_insensitive(self):

        class ExampleEnum(Enum):
            First = 1

        field = StringEnumField(
            {},
            {"ONE": ExampleEnum.First},
        )

        self.assertEqual(
            ExampleEnum.First,
            field.to_internal_value("oNe")
        )
