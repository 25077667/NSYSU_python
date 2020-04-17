from PyPA3 import *
def testNums():
    print('printf("%i,%+i,%5i,%+05i\\n",1,2,-3,4.5):')
    print("√ = 1,+2,   -3,+0004\n? = ",end="")
    printf("%i,%+i,%5i,%+05i\n",1,2,-3,4.5)

    print('\nprintf("%f,%+f,%5f,%+05f\\n",1,2,-3,4.5):')
    print("√ = 1.000000,+2.000000,-3.000000,+4.500000\n? = ",end="")
    printf("%f,%+f,%5f,%+05f\n",1,2,-3,4.5)

    print('\nprintf("%j,%+j,%5j,%+05j\\n",1,2,-3,4.5):')
    print("√ = 1+0j,2+0j,   -3+    0j,00004+00000j\n? = ",end="")
    printf("%j,%+j,%5j,%+05j\n",1,2,-3,4.5)

    print('\nprintf("%j,%+j,%5j,%+05j\\n",1j,2j,-3j,4.5j):')
    print("√ = 1j,0+2j,   -3j,00000+00004j\n? = ",end="")
    printf("%j,%+j,%5j,%+05j\n",1j,2j,-3j,4.5j)

    print('\nprintf("%1.0j,%+5.2j,%5.5j,%+05.1j\\n",1j,2j,-3j,4.5j):')
    print("√ = 1j, 0.00+ 2.00j,-3.00000j,000.0+004.5j\n? = ",end="")
    printf("%1.0j,%+5.2j,%5.5j,%+05.1j\n\n",1j,2j,-3j,4.5j)

if (__name__=="__main__"):
    testNums()
