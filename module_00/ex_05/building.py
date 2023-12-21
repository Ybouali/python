import string
import sys


def __numberCharUpperInString(text):

    """
        Calculate the number of the upper case characters in a string
    """
    count = 0

    for c in text:
        if c.isalpha() is True and c.isupper() is True:
            count += 1
    return count


def __numberCharLowerInString(text):

    """
        Calculate the number of the lower case characters in a string
    """
    count = 0

    for c in text:
        if c.isalpha() is True and c.isupper() is False:
            count += 1
    return count


def __numberSpaceInString(text):

    """
        Calculate the number of the space characters in a string
    """
    count = 0

    for c in text:
        if c.isspace() is True:
            count += 1
    return count


def __checkForPunctuationMarks(c) -> bool:

    pun_set = set(string.punctuation)

    for p in pun_set:
        if p is c:
            return True

    return False


def __numberPunctuationInString(text):

    """
        Calculate the number of Punctuation in a string
    """
    count = 0

    for c in text:
        if __checkForPunctuationMarks(c):
            count += 1
    return count


def __numberDigitsInString(text):

    """
        Calculate the number of Digits in a string
    """
    count = 0

    for c in text:
        if c.isdigit() is True:
            count += 1
    return count


def text_analyzer(text):

    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """

    if text.isnumeric() is True:
        raise AssertionError("Error:\nArgument is not a string")

    if text == '':
        raise AssertionError("Error:\nThe string must not be empty")

    toReturn = "The text contains " + str(len(text)) + " character(s): \n"

    # get the number of upper characters
    nCharUpper = __numberCharUpperInString(text)

    # get the number of lower characters
    nCharLower = __numberCharLowerInString(text)

    # get the number of space characters
    nSpace = __numberSpaceInString(text)

    # get the number of punctuation characters
    nPunctuation = __numberPunctuationInString(text)

    # get the number of digits characters
    nDigits = __numberDigitsInString(text)

    # concatenate the the string to return it

    toReturn += "- " + str(nCharUpper) + " upper litter(s) \n"

    toReturn += "- " + str(nCharLower) + " lower litter(s) \n"

    toReturn += "- " + str(nPunctuation) + " Punctuation mark(s)\n"

    toReturn += "- " + str(nSpace) + " space(s) \n"

    toReturn += "- " + str(nDigits) + " digits(s)"

    return toReturn


def __argvToString(argv):

    """
        Concatenate a array 2d of arguments
    """
    avStr = ""

    for arg in argv:
        avStr += " " + str(arg)
    return avStr


def main():

    try:
        text = "Hello World! "

        # if there is no args provided as default the arguments will be the text
        if len(sys.argv) < 2:

            print(f"What is the text to count?\n{text}")

        # if there is more than one arg
        elif len(sys.argv) > 2:

            text = __argvToString(sys.argv)

        # if there is one arg
        else:

            text = sys.argv[1]

        print(text_analyzer(text))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
