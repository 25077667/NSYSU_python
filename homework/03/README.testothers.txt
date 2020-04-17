You should read the README.PyPA3.txt and README.testnums.txt files before
you read this file.

This README.testothers.txt file describes the way that the remaining types
will print. There are some special changes that need to be emphasized:
 - The dictionary datatype will display with a different pair of symbols: 
    >>> printf("%D\n",{1:2,3:4,5:6})
    «1: 2, 3: 4, 5: 6»
    >>> print({1:2,3:4,5:6})
    {1: 2, 3: 4, 5: 6}
    >>>

    What are these "«" and "»" symbols? They are unicode characters that you
    can't type directly on your keyboard. Python3 strings are all unicode,
    however, so there will be no problem in using them. But if you cannot 
    type them, then how to put them into you program? Answer: cut and paste
    these characters from this current sentence, where I show them to you
    right here: « ». 

  - Since the dictionary doesn't printf with the "{...}" symbols, there is
    no confusion with sets. So the empty set will display as "{}" (not as
    "set()".

  - Similarly, since complex numbers don't use parentheses (see the
    README.testnums.txt file), there is no confusion when tuples use 
    parentheses. So the singleton tuple prints without a comma at the end.
    >>> printf("%T\n",((2j),))
    (2j)
    >>>

    (In actual fact, to make the assignment shorter, we won't really implement
     the nested aspect of this idea. So, even though a complex number won't
     have parentheses around it, a complex number inside of a list or tuple 
     can:
     >>> printf("%T   %T   %L\n",(0j,), ((1+2j),), [3+4j])
     (0j)  ((1+2j))   [(3+4j)]
     >>> print(((0j),),(1+2j,),[3+4j])
     (0j,) ((1+2j),) [(3+4j)]
     >>>
     Our solution to not recursively applying the rules? To not test such
     cases.)

So now, with these special rules explained, how do the various formats work?
They all work, essentially, like strings. Recall that this is how strings work:
%s:   Print as a string.
%ns:  Print the string using at least n positions, and align the string to
      right-side of these n positions.
%-ns: Print the string using at least n positions, and align the string to
      left-side of these n positions.

In the above, note that some people get confused when they have a string of 
more than n characters. For example, see that there is no difference between
any of the following:
>>> printf("%s,%3s,%-3s\n","Hello","Hello","Hello")
Hello,Hello,Hello
>>>

So then, what about all of the format types other than %s? Well they are as
follows:

%B: Convert the boolean to a string then print according to %s formatting.
%nB: Convert the boolean to a string then print according to %ns formatting.
%-nB: Convert the boolean to a string then print according to %-ns formatting.

%L,%nL,%-nL: Convert the list to a string, then use the string formatting.

%T,%nT,%-nT: Convert the tuple to a string, then use the string formatting,
             but remember that singletons lose their ",".

%S,%nS,%-nS: Convert the set to a string, then use the string formatting,
             but remember that empty sets display as "{}".

%D,%nD,%-nD: Convert the dictionary to a string, then use the string           
             formatting, but remember to replace the "{" and "}" symbols.

The only complexity of the above is that printf() will verify that that the
object is of the indicated type before converting to a string. But the %a
doesn't require such a verification, but it will convert any type to a string:

%a,%na,%-na: Convert any type to a string, then use the string formatting
             rules.

These rules weren't as complicated as those for numbers. So now how to test
them? Well I have provided three testing files:

The "testTypes.py" file tests for "%s", "%L", "%T", "%D", and "%B". The last 
two lines of the file allow it to be tested as a stand-alone program:
  if (__name__=="__main__"):
      testTypes()

The "testAny.py" file provides tests for various types using "%a". The last
two lines of this file allow it also to be tested as a stand-alone program.

The "testSpecials.py" file provides tests for special cases, including some
that are meant to cause errors. Therefore, to test a given printf(), you'll
need to comment out any earlier printfs that are causing an error. This
testSpecials.py file is also designed to testable as a stand-alone program.

Now that you have seen all of the format rules, you can proceed to the
README.implementation.txt file...


