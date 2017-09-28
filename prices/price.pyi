from .amount import Amount, Numeric

class Price:
    net = ...  # type: Amount
    gross = ...  # type: Amount

    def __init__(self, net: Amount, gross: Amount) -> None: ...

    def __repr__(self) -> str: ...

    def __lt__(self, other: Price) -> bool: ...

    def __le__(self, other: Price) -> bool: ...

    def __gt__(self, other: Price) -> bool: ...

    def __ge__(self, other: Price) -> bool: ...

    def __eq__(self, other: object) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    def __mul__(self, other: Numeric) -> Price: ...

    def __rmul__(self, other: object) -> Price: ...

    def __truediv__(self, other: Numeric) -> Price: ...

    def __div__(self, other: Numeric) -> Price: ...

    def __add__(self, other: Price) -> Price: ...

    def __sub__(self, other: Price) -> Price: ...

    def __bool__(self) -> bool: ...

    def __nonzero__(self) -> bool: ...

    @property
    def currency(self) -> str: ...

    @property
    def tax(self) -> Amount: ...

    def quantize(self, exp: str=None, rounding: str=None) -> Price: ...
