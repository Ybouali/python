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


def __numberPunctuationInString(text):

    """
        Calculate the number of Punctuation in a string
    """
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

    print(f"------------------------------->({len(text)})")

    toReturn = "The text contains " + str(len(text)) + " character(s): \n"

    # get the number of upper characters
    nCharUpper = __numberCharUpperInString(text)

    # get the number of lower characters
    nCharLower = __numberCharLowerInString(text)

    # get the number of space characters
    nSpace = __numberSpaceInString(text)

    # get the number of punctuation characters
    nPunctuation = __numberPunctuationInString(text)

    toReturn += "- " + str(nCharUpper) + " upper litter(s) \n"

    toReturn += "- " + str(nCharLower) + " lower litter(s) \n"

    toReturn += "- " + str(nSpace) + " space(s) \n"

    toReturn += "- " + str(nPunctuation) + " Punctuation mark(s)"

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
        if len(sys.argv) != 2:
            raise AssertionError("You must provide one string argument")

        # i comented this because is not required by the subject
        # text = __argvToString(sys.argv)

        print(text_analyzer(text=sys.argv[1]))

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()