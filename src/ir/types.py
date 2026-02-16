from enum import Enum


class LoweringError(Exception):
    pass


class Type(Enum):
    INDEX = "index"
    BIGINT = "bigint"
