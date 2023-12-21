from types import NoneType
from typing import Any

def __NULL_not_found(object: Any) -> bool:

    if isinstance(object, NoneType):
        return False
    
    if isinstance(object, float) and m.isnan(object):
        return False

        if isinstance(object, int) and object == 0:

            print(f"Zero: {object} {type(object)}")

            return 0

        if isinstance(object, str) and len(object) == 0:

            print(f"Empty: {object} {type(object)}")

            return 0

def ft_filter(func, iterable):

    """
        ft_filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true.
    """

    print (type(iterable))

    if isinstance(func, NoneType):
        return iterable


    for i in iterable:
        if func(i) is True:
            print (f"Filter ({i})")

def is_even(n) -> bool:
    return bool(n % 2)

def main():
    try:
        numbers = [1, 2, 3, 4, 5]

        evens_numbers = filter(None, numbers)
        ft_evens_numbers = ft_filter(None, numbers)

        print (list(evens_numbers))
        print (ft_evens_numbers)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()