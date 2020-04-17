You should read the README.PyPA3.txt, README.testnums.txt and README.others.txt
files before you read this file.

This README.implementation.txt file provides the requirements and guidance for
implementing the PyPA3.py file.

Line 1: This line creates a dictionary of the three number types (not counting
        booleans). This is a very special dictionary, because it helps us to
        understand what we have always been saying: in Python EVERYTHING is an
        object. In this dictionary, the keys will be the datatypes. That is a
        strange idea, but it works. The values will be the letters "i", "f",
        and "j". With this dictionary, we will be able to match the various 
        number types to their format letters.
 
Line 2: This line is similar to Line 1. It is for the other datatypes. But, in
        this case, the keys are the letters and the values are the datatypes.
        In other words, the keys are: "s", "L", "T", "S", "D", and "B".

Line 3: empty

Lines 4-19: Copy and paste these lines exactly as shown here:
def doIfMatches(A,B):
    """This checks if the datatype for object A matches to the format string B
       (which means that it checks whether the last character of B indicates
       the datatype of object A).
       If they don't match, an error is printed and the program exits. 
         Note: there are better solutions than running "exit()", but we haven't
               learned those solutions yet, so you must just use exit(). (This
               is also true for all places below, where errors are detected.)
       If they do match, then:
        - The variable A is converted to a string.
        - If:
           - it is a dictionary, the {} symbols are converted to «» symbols.
           - it is a singleton tuple, the , is removed
           - it is an empty set, it becomes "{}"
        - Then print the string, according to the format of B (but B's last
          letter needs to first be converted to "s").                       """

Line 20-X: Using as many lines as you want, implement doIfMatches() so that it
           follows the rules indicated in its above docstring.
           Note: You will use print("..."%(...)) in your implementation.

Line X+1:def putfORi(S): return __1__
         This is a 1-line function. It takes a format string S (eg, "%.1j")
         and looks to see if S contains a ".". If it does contain one, then the
         function will return S, but with the last character replaced by a "f".
         If it does not contain one, then it will return S, but with the last
         character replaced with an "i".
         Although there are many ways to implement this, I require you to use a
         logic expression such as those described on slides 36-41 of Lecture 4.
         Note: you cannot use an "if" or a ";" in your implementation of __1__.

Line X+2: empty

Line (X+3)-(X+14):
def handleNumbers(A,B):
    """This receives a number A and a format string B. The format string is 
       known to end in either "i", "f", or "j".
       If B ends in a "j" then:
        - The format string B is updated by calling putfORi(B)
        - The real part of A is printed by the format of B, but only if either:
           1)it is nonzero or 2)the string B has a "+" in it.
        - The imaginary part always prints. It will have a "+" or "-" in front 
          of it if the real part was printed; otherwise it will only have a "-"
           if it is negative. The imaginary part is always followed by a "j".
       If B ends in "i" or "f" then A is simply printed according to the format
       rule of B.                                                           """
    
Line (X+15)-Y: Using as many lines as you want, implement handleNumbers() so
               that it follows the rules indicated in its above docstring.
               Note: You will use print("..."%(...)) in your implementation.

Lines Y-(Y+37)
def fprint(__1__,__2__,__3__):
    """This receives a single format string, a variable-length argument, and a
       special keyword-only variable with the default value of a singleton list
       holding the number 0.
       -In saying "a single format string" we mean that the string begins with 
        a "%" and ends with a letter, with no letters or "%" in the middle.
          (But there are two special format strings: "*" and "?". A "*" 
           indicates that a new printf() has begun, so that the counter needs 
           to reset to 0.
           A "?" indicates that this printf() has finished, so we need to check
           for unmatched extra objects in the provided list.)
       -As for the variable-length argument, it holds all of the arguments you
        give to printf(), beyond the first argument, which is a format string.
       -What is the special variable? In slides 76-90 of Lecture 6, we learned
        that mutable default types persist between calls to a function. So the
        value of 0 in this list can be update to 1, 2, 3, etc. and that change
        will persist.
        Thus, we can look into this value to find the index in the variable-
        length argument tuple.

        Now for the behavior:
        - If the format string is finished (ie, you receive a "?"), but the
          argument list is not completed (ie, the counter held in the special
          variable has not reached to the end of the variable-length argument
          tuple), then you print an error message and then exit().
        - If the argument list is finished, but there is a new format string,
          print an error message and then exit().
        - Copy the next value in the variable-length tuple to the name "me". 
        - If the format string ends in "a" and if the variable named "me" 
          holds a number, then convert into a string. Note: you must use the
          dictionary defined on Line #1 to do this. 
        - If the format string ends in "a" then use the dictionary defined on 
          Line #2 to replace the "a" with the appropriate letter for the 
          datatype of the variable "me". Note that if "me" had been a number, 
          it would by now be a string.
        - If the datatype of the value stored in "me" is a number, then call
          handleNumbers(). Otherwise, call doIfMatches().                   """
    
Line (Y+38)-Z: Using as many lines as you want, implement fprint() so that it
               follows the rules indicated in its above docstring.

Line (Z+1)-(Z+17)
def printf(__1__):
    """This implements the printf() function. It receives a variable number of
       arguments (including perhaps zero arguments, indicating to do nothing).

       The behavior is to walk through the format string passed in as the first
       argument, looking for "%" symbols. When one is found, we keep looking
       to find the next letter. The characters in between are a single format
       string. We can then call fprint() to handle the printing of this current
       argument.
       There are some considerations:
         - "%%" is not a format string, but just the way to print a "%".
         - In calling fprint(), it needs to be initialized first, by passing in
           a "*". This is because we may do more than one printf().
         - When finished, we need to check that we didn't finish with an
	   unmatched %.
         - When finished, we need to call fprint() again with a "?" to ensure
           that there were no extra arguments.                              """

Line (Z+18)-?: Using as many lines as you want, implement printf() so that it
               follows the rules indicated in its above docstring.

The final 9 lines: 
if __name__ == "__main__":
    from testNums import *
    from testTypes import *
    from testAny import *
    from testSpecials import *
    testNums()
    testTypes()
    testAny()
    testSpecials()

The above final lines allow you to run "python3 PyPA3.py" to do all of the
provided tests at once. Of course you can also import printf from PyPA3, to
use it in other programs.
