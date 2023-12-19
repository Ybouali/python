import string
import sys


def __numberCharUpperInString(text):
    count = 0

    for c in text:
        if c.isupper() is True and c.isspace() is False:
            count += 1
    return count


def __numberCharLowerInString(text):
    count = 0

    for c in text:
        if c.isupper() is False and c.isspace() is False:
            count += 1
    return count


def __numberSpaceInString(text):
    count = 0

    for c in text:
        if c.isspace() is True:
            count += 1
    return count


def __numberPunctuationInString(text):
    count = 0

    for c in text:
        if c in string.punctuation:
            count += 1
    return count


def text_analyzer(text):

    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """

    if text.isnumeric() is True:
        raise AssertionError("argument is not a string")

    toReturn = "The text contains " + str(len(text)) + " character(s): \n"

    nCharUpper = __numberCharUpperInString(text)

    nCharLower = __numberCharLowerInString(text)

    nSpace = __numberSpaceInString(text)

    nPunctuation = __numberPunctuationInString(text)

    toReturn += "- " + str(nCharUpper) + " upper litter(s) \n"

    toReturn += "- " + str(nCharLower) + " lower litter(s) \n"

    toReturn += "- " + str(nSpace) + " space(s) \n"

    toReturn += "- " + str(nPunctuation) + " Punctuation mark(s)"

    return toReturn


def __argvToString(argv):
    avStr = ""

    for arg in argv:
        avStr += " " + str(arg)
    return avStr


try:
    if len(sys.argv) != 2:
        raise AssertionError("You must provide one string argument")

    # text = __argvToString(sys.argv)

    print(text_analyzer(text=sys.argv[1]))

except Exception as e:
    print(e)
