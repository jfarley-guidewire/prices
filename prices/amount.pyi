import decimal

from typing import Union, overload


Money = Union[int, decimal.Decimal]
Numeric = Union[int, decimal.Decimal]


class Amount:
    value = ...  # type: decimal.Decimal
    currency = ...  # type: str

    def __init__(self, value: Money, currency: str) -> None: ...

    def __repr__(self) -> str: ...

    def __lt__(self, other: Amount) -> bool: ...

    def __le__(self, other: Amount) -> bool: ...

    def __gt__(self, other: Amount) -> bool: ...

    def __ge__(self, other: Amount) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    def __mul__(self, other: Numeric) -> Amount: ...

    def __rmul__(self, other: object) -> Amount: ...

    @overload
    def __truediv__(self, other: Numeric) -> Amount: ...
    @overload
    def __truediv__(self, other: Amount) -> decimal.Decimal: ...

    @overload
    def __div__(self, other: Numeric) -> Amount: ...
    @overload
    def __div__(self, other: Amount) -> decimal.Decimal: ...

    def __add__(self, other: Amount) -> Amount: ...

    def __sub__(self, other: Amount) -> Amount: ...

    def __bool__(self) -> bool: ...

    def __nonzero__(self) -> bool: ...

    def quantize(self, exp: str=None, rounding: str=None) -> Amount: ...
