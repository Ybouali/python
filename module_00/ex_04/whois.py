import sys

try:

    if (len(sys.argv) != 1):

        if (len(sys.argv) > 2):
            raise AssertionError("AssertionError: more than one \
                                 argument are provided")

        if (sys.argv[1].isdigit() is False):
            raise AssertionError("AssertionError: argument is not an integer")

        number = int(sys.argv[1])

        if (number is 0):
            print("I'm Zero.")
        elif (number % 2 is 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")

except Exception as e:
    print(e)
