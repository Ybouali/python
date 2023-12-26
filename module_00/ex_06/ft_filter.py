from types import NoneType


def ft_filter(__func, __iterable):

    """
        ft_filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of \
            iterable for which function (item)
        is true. If function is None, return the items that are true.
    """

    # list to return
    to_return = []

    # check if the is no function return the iterable
    if isinstance(__func, NoneType):
        return __iterable

    # loop through the elements of iterable and check if the function
    # returns True so add the item to to_return list
    for i in __iterable:
        if __func(i) is True:
            to_return.append(i)

    return iter(to_return)


def is_even(n) -> bool:
    return bool(n % 2)


def main():
    try:
        numbers = [1, 2, 3, 4, 5]

        evens_numbers = filter(is_even, numbers)
        ft_evens_numbers = ft_filter(is_even, numbers)

        print(list(evens_numbers))
        print(list(ft_evens_numbers))

        evens_numbers_1 = filter(None, numbers)
        ft_evens_numbers_1 = ft_filter(None, numbers)

        print(list(evens_numbers_1))
        print(list(ft_evens_numbers_1))

        evens_numbers_2 = filter(None, [])
        ft_evens_numbers_2 = ft_filter(None, [])

        print(list(evens_numbers_2))
        print(list(ft_evens_numbers_2))

        nums = [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]

        odd = filter(lambda p: p % 2 != 0, nums)
        ft_odd = ft_filter(lambda p: p % 2 != 0, nums)

        print(list(odd))
        print(list(ft_odd))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
