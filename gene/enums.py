from enum import IntEnum


class BaseEnum(IntEnum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def values(cls):
        return [key.value for key in cls]


class GeneStatus(BaseEnum):
    PENDING = 1
    VERIFIED = 2
    EXTRACTED = 3
    PACKAGED = 4
    DECODED = 5
    CANCELED = 6


class GeneLocation(BaseEnum):
    GENETICA = 1
    HANOI_LAB = 2
    SHIPPING_DEPARTMENT = 3
    USA_LAB = 4


class GeneActivityType(BaseEnum):
    CREATE = 0
    VERIFY = 1
    EXTRACT = 2
    PACKAGE = 3
    DECODE = 4
    SEND_TO_GENETICA = 5
    SEND_TO_HANOI_LAB = 6
    SEND_TO_USA_LAB = 7
    SEND_TO_SHIPPING = 8
    CANCEL = 9
