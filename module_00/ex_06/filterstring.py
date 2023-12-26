import sys

def main():
    try:
        # make sure that we have 2 arguments
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        
        # make sure the secound argument is a int variable
        try: 
            req_len = int(sys.argv[2])
        except Exception as e:
            raise AssertionError("AssertionError: the arguments are bad")

        # get the string 
        str_data = sys.argv[1]

        # split the string by spaces
        list_words = str_data.split(" ");

        to_print = []

        # loop through the words and add the needed word to the list
        # the word needed mean's has the length greater than req_len
        for word in list_words:
            if len(word) > req_len:
                to_print.append(word)

        print(to_print)

    except Exception as e:
        print (e)

if __name__ == "__main__":
    main()