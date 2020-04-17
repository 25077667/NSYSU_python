You should read the README.PyPA3.txt file before you read this file.

This README.testnums.txt file describes the 3 number types (excluding booleans). 
They are:

%i: This works just as it does with Python's % operator:
     %+i: Include the number's sign even if it is positive.
          Eg, printf("%i,%+i,%i,%+i!\n",1,1,-1,-1)  => 1,+1,-1,-1!
     %ni: Use at least n positions in printing the number.
          Eg, printf("%3i,%3i,%3i!\n",100,1,10000) => 100,  1,10000!
     %0ni:Pad front with zeroes to use atleast n positions to print the number.
          Eg, printf("%03i,%03i,%03i!\n",1,-1,10000) => 001,-01,10000!
     %+0ni:Combines all of the above.
          Eg, printf("%+03i,%+03i,%+03i!\n",1,-1,10000) => +01,-01,+10000!

%f: This works just as it does with Python's % operator:
     %+f: Include the number's sign even if it is positive. 
     %ni: Use at least n positions in printing the number.
     %0ni:Pad front with zeroes to use atleast n positions to print the number.
     %.n: Print n decimal places. (Unless you use this, the default is 6.)
          These can, of course, combine:
          >>> printf("X%10f,%010f,%+010f!\n",1.1,2.2,3.3)
          X  1.100000,002.200000,+03.300000!
          >>> printf("%.2f,%6.2f,%+6.2f!\n",1.1,2.2,3.3)
          1.10,  2.20, +3.30!

%j: This one has a more "complex" behavior. Consider:
    >>> printf("Notice no () around %j!\n",3+4j) => Notice no () around 3+4j!

    From the above, we see a significant change from Python's way of printing
    complex numbers: we don't show parentheses.

    We also need to discuss how formatting works on complex numbers.
    The key idea is that you can only specify one format to be used for both
    the real and complex parts. If the format has no "." then it follows the
    %i rules:
    >>> printf("%03j,%3j,%j\n",1.2+3.4j,5,6+7j)
    001+003j,  5+  0j,6+7j
    >>>
    But if there is a "." in the format, then it follows the %f rules:
    >>> printf("%05.1j,%5.1j,%.1j\n",1.2+3.4j,5,6+7j) 
    001.2+003.4j,  5.0+  0.0j,6.0+7.0j
    >>>

    There is one exception to the above system, however. The + symbol will not
    indicate the inclusion of the sign bit. Instead it indicates that the
    real-part must be given. This rule is to handle fully imaginary numbers:
    >>> printf("%j,%j,%j,%+j,%+.1j\n",0,1j,2+1j,1j,2+1j)
    0j,1j,2+1j,0+1j,2.0+1.0j
    >>>
    
    See how the real part doesn't show up if the number is fully imaginary
    (unless we include the "+"). Recall that Python has a similar rule:
    >>> print(complex(0), 1j, 2+1j,sep=",")
    0j,1j,(2+1j)
    >>>

So those are the rules for numbers. I have provided a file, "testnums.py". 
This file shows the expected outputs of various number formats. If you look
at the file, you will see that it has triplets of two print()s followed by 
one printf(). Look at the first five lines of the file:
from PyPA3 import *
def testNums():
    print('printf("%i,%+i,%5i,%+05i\\n",1,2,-3,4.5):')
    print("√ = 1,+2,   -3,+0004\n? = ",end="")
    printf("%i,%+i,%5i,%+05i\n",1,2,-3,4.5)
    ...

See above that it loads in your PyPA3.py file. This allows printf() to work.
See also that the first print() displays what printf() arguments are being
tested.  And see that the second print() shows what the proper output should 
look like. If you implement the programming assignment correctly, then the
third line will create the same output as the print("√ = ...") line creates.
In fact, even if you have not implemented anything except the %i, this 
printf() will work. 

Looking through the testnums.py file, it tests various %f and %j situations.
The final lines of the file allow it to be run as a stand-alone program. Here
are the last two lines:
if (__name__=="__main__"):
    testNums()

So that means that you can type "python3 testnums.py" and you will run all of
the number tests. If you pass all these tests, your treatment of numbers will
have been minimally tested. We will test other numbers, but they will probably
also work if the provided tests are all working.

Now that you understand about numbers, proceed to reading README.testothers.txt
