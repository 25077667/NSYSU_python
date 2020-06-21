from PyPA5 import *


def testSpecials():
    printf('''Backslashes are handled automatically, because printf receives each of the 
    following as just one character: tab:\t, backslash:\\, newline:\n''')
    printf('This is how you get a "%%" symbol.\n')
    printf('The following line will do nothing:\n')
    printf()
    printf('Any of the following lines will crash:\n')
    try:
        printf('%')
    finally:
        try:
            printf('%s')
        finally:
            try:
                printf('%Q')
            finally:
                try:
                    printf('%', 1)
                finally:
                    try:
                        printf('%Q', 1)
                    finally:
                        try:
                            printf('%s', '1', '2')
                        finally:
                            try:
                                printf('1', '2')
                            finally:
                                print("Test spetial finished!")


if (__name__ == "__main__"):
    testSpecials()
