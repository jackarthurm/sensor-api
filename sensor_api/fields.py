from enum import Enum
from typing import (
    Mapping,
    Optional,
    Any,
)

from rest_framework.fields import Field


class StringEnumField(Field):
    """A simple serializer field which uses a forward and
    a reverse mapping to serialize enum values to string
    and vice-versa
    Implemented as case-insensitive
    """

    default_error_messages = {
        "invalid_enum": '"{input}" does not map to an enum value.'
    }

    def __init__(
        self,
        to_representation_mapping: Mapping[Enum, str],
        to_internal_value_mapping: Mapping[str, Enum],
        *args,
        **kwargs
    ):
        super(StringEnumField, self).__init__(*args, **kwargs)

        self._to_representation_mapping = to_representation_mapping
        self._to_internal_value_mapping = {
            k.lower(): v for k, v in to_internal_value_mapping.items()
        }

    def to_internal_value(self, data: Any) -> Enum:

        try:
            return self._to_internal_value_mapping[str(data).lower()]
        except KeyError:
            self.fail("invalid_enum", input=data)

    def to_representation(self, value: Optional[Enum]) -> Optional[str]:

        if value is None:
            return None

        return self._to_representation_mapping.get(value)
