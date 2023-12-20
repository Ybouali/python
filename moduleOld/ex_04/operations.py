from curses.ascii import isdigit
import sys


class Operation:
    """
        Operation Class will do the operations
        And prepare the result as a string

        Attributes:
            number1 (int): the first number for the operation
            number2 (int): the secound number for the operation
    """
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2
        self.__Sum = 0
        self.__Difference = 0
        self.__Product = 0
        self.__Quotient = 0
        self.__Remainder = 0

    def __operation(self):
        """
            Operation method will store the result of the operations
        """

        # Product operation
        self.__Product = self.number1 * self.number2

        # Difference operation
        self.__Difference = self.number1 - self.number2

        # Sum operation
        self.__Sum = self.number1 + self.number2

        # Quotient operation if the secound number is not a zero number
        if self.number2 != 0:
            self.__Quotient = self.number1 / self.number2

        # Remainder operation if the secound number is not a zero number
        if self.number2 != 0:
            self.__Remainder = self.number1 % self.number2

    def __str__(self):

        # Call the operation method
        self.__operation()

        # error message for div
        errorDivision = "ERROR (division by zero)"

        # error message for Qoutient
        errorQoutient = "ERROR (modulo by zero)"

        # preaper the string for the Qoutient and Remainder
        otherString = f"Quotient:      {self.__Quotient}\n\
            Remainder:     {self.__Remainder}"

        # if the number2 is zero so we should set the error massage
        if self.number2 == 0:
            otherString = f"Quotient:      {errorDivision}\n\
                Remainder:     {errorQoutient}"

        # return of the string result
        return f"Sum:           {self.__Sum} \n\
            Difference:    {self.__Difference}\n\
            Product:       {self.__Product}\n{otherString}"


try:
    if len(sys.argv) == 1:

        print("Usage: python operations.py <number1> <number2>")

        print("Example:\n\
                    python operations.py 10 3")

        exit()

    # Check if there is more than tow numbers provided
    if len(sys.argv) > 3:
        raise AssertionError(f"AssertionError: too many arguments")

    # Check if there is tow numbers provided
    if len(sys.argv) != 3:
        raise AssertionError(f"U must provide tow numbers\nExample:\n\
                    python operations.py 10 3")

    # Check that the arguments are are digits
    if sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
        raise AssertionError("AssertionError: only integers")

    # get the first number
    firstNumber = int(sys.argv[1])

    # get the secound number
    secoundNumber = int(sys.argv[2])

    # init  the class Operation
    result = Operation(number1=firstNumber, number2=secoundNumber)

    print(result)

except Exception as e:
    print(e)
