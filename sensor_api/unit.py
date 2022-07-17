from abc import (
    ABC,
    abstractmethod,
)
from numbers import Real


class Unit(ABC):
    """Abstract class for a unit used to quantify some physical quantity"""

    @abstractmethod
    def to_si(self, value: Real) -> Real:
        pass

    @abstractmethod
    def from_si(self, value: Real) -> Real:
        pass


class LinearUnit(Unit, ABC):
    """A unit which can be converted from and to SI via a scaling followed by an offset"""

    def __init__(
        self,
        from_si_scale_factor: Real,
        from_si_offset: Real
    ) -> None:

        self._from_si_scale_factor = from_si_scale_factor
        self._from_si_offset = from_si_offset

    def to_si(self, value: Real) -> Real:
        return (value - self._from_si_offset) / self._from_si_scale_factor

    def from_si(self, value: Real) -> Real:
        return value * self._from_si_scale_factor + self._from_si_offset


class SIUnit(Unit, ABC):

    def to_si(self, value: Real) -> Real:
        return value

    def from_si(self, value: Real) -> Real:
        return value
