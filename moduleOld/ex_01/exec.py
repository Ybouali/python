import sys

try:
    if (len(sys.argv) > 1):
        str = ""

        # get all the args in one string
        for i in range(len(sys.argv)):
            if (i != 0):
                # swapcase used to reverse the string format
                str += sys.argv[i].swapcase()
                if (i != len(sys.argv) - 1):
                    str += " "

        # get the len of the str
        revStr = str[::-1]

        # print the result
        print(revStr)

except Exception as e:
    print(e)
