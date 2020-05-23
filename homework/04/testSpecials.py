from PyPA4 import *


def testSpecials():
    printf('''Backslashes are handled automatically, because printf receives each of the 
    following as just one character: tab:\t, backslash:\\, newline:\n''')
    printf('This is how you get a "%%" symbol.\n')
    printf('The following line will do nothing:\n')
    printf()
    printf('Any of the following lines will crash:\n')
    # printf('%')
    # printf('%s')
    # printf('%Q')
    # printf('%', 1)
    # printf('%Q', 1)
    # printf('%s', '1', '2')
    printf('1', '2')


if (__name__ == "__main__"):
    testSpecials()
