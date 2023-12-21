import math as m
from types import NoneType
from typing import Any


def NULL_not_found(object: Any) -> int:
    try:
        if isinstance(object, NoneType):

            print(f"Nothing: {object} {type(object)}")

            return 0

        if isinstance(object, float) and m.isnan(object):

            print(f"Cheese: {object} {type(object)}")

            return 0

        if isinstance(object, int) and object == 0:

            print(f"Zero: {object} {type(object)}")

            return 0

        if isinstance(object, str) and len(object) == 0:

            print(f"Empty: {object} {type(object)}")

            return 0

        else:

            print("Type not found")

            return 1

    except Exception as e:
        print(e)
