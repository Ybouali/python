from curses.ascii import isdigit
import sys

class Operation:
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
            operation function will return the result of the operation that is provided in the argument
        """

        self.__Product = self.number1 * self.number2
        
        
        self.__Difference = self.number1 - self.number2
        
        self.__Sum = self.number1 + self.number2

        if self.number2 != 0:
            self.__Quotient = self.number1 / self.number2
        
        if self.number2 != 0:
            self.__Remainder = self.number1 % self.number2
    
    def __str__(self):

        self.__operation()

        errorDivision = "ERROR (division by zero)"

        errorQoutient = "ERROR (modulo by zero)"


        otherString = f"Quotient:      {self.__Quotient}\nRemainder:     {self.__Remainder}"


        if self.number2 == 0:
            otherString = f"Quotient:      {errorDivision}\nRemainder:     {errorQoutient}"
            

        return f"Sum:           {self.__Sum} \nDifference:    {self.__Difference}\nProduct:       {self.__Product}\n{otherString}" 


try:
    
    if len(sys.argv) == 1:
    
        print("Usage: python operations.py <number1> <number2>")

        print("Example:\n\
                    python operations.py 10 3")

        exit()

    if len(sys.argv) > 3:
        raise AssertionError(f"AssertionError: too many arguments")
    if len(sys.argv) != 3:
        raise AssertionError(f"U must provide tow numbers\nExample:\n\
                    python operations.py 10 3")

    if sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
        raise AssertionError("AssertionError: only integers")

    # get the first number
    firstNumber = int(sys.argv[1])

    secoundNumber = int(sys.argv[2])

    result = Operation(number1=firstNumber, number2=secoundNumber)
    
    print(result)

except Exception as e:
    print(e)
