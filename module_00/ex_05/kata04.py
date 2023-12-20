import os
kata = (0, 4, 132.42222, 10000, 12345.67)


def __find_by_character(character, list_strings):
    for string in list_strings:
        if character in string:
            return string
    return None


def __fromat_math(n):
    return "{:.2e}".format(n)


try:
    listDirProject = os.listdir('../../')

    listDirModule = os.listdir('../')

    first_element = __find_by_character(str(kata[0]), listDirProject)

    secound_element = __find_by_character(str(kata[1]), listDirModule)

    third_element = round(float(kata[2]), 2)

    fourth_element = __fromat_math(kata[3])

    fiveth_element = __fromat_math(kata[4])

    print(f"{first_element} , {secound_element} : \
          {third_element}, {fourth_element}, {fiveth_element}")

except Exception as e:
    print(e)
#  python kata05.py | cut -c 11,19
