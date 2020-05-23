                             Programming in Python
                           Programming Assignment #4

Due date: Tuesday, May 26, at 11:59pm. 

Submission rules: Submit two files, "PyPA4.py" and "testSpecials.py".
                  The first line of each file must be a comment that is
		  exactly only your student ID.

Rules against: As in all of the homeworks, it is a severe mistake to cheat.
cheating       This does only mean to not copy, it also means:
                - To not let people copy FROM you.
                - To not let others see your code.
                - To not tell others how to do part of the assignment, in
                  detail. (General guidance to a classmate is allowed. The key
                  idea that divides allowed help from cheating is that study
                  groups are helpful for learning, but copying work is not.)
               Students caught cheating will fail the course -- both the one
               who copies and the one who lets another copy from them.

Assignment Overview:
In this assignment, we will improve our printf() function to handle new types
and to print error messages. Consider the following program's output:

% cat testnewtypes.py
from PyPA4 import *
printf("Print as %%S: %S $S\n",{1,2},frozenset({3})) #frozenset converts to set
printf("Print as %%Z: %Z $Z\n",{1,2},frozenset({3})) #set converts to frozenset
printf("Print as %%s: %s\n",'Hello')
printf("Print as %%b: %b %b\n", b'Hello', bytearray(b'Bye')) # Convertable
printf("Print as %%y: %y %y\n", bytearray(b'Hello'), b'Bye') # Convertable
printf("This will crash: %s\n",b'Hello') #bytes aren't equal to strings
%
% python3 testnewtypes.py
Print as %S: {1,2} {3}
Print as %Z: ⦓1,2⦔ ⦓3⦔
Print as %s: Hello
Print as %b: ‘Hello’ ‘Bye’
Print as %y: “Hello” “Bye”
This will crash: Traceback (most recent call last):
  File "testnewtypes.py", line 7, in <module>
    printf("This will crash: %s\n",b'Hello') #bytes aren't equal to strings
  File "_____/PyPA4.py", line ___, in printf
    _______________________________________________
TypeError: format string expects str, not bytes
%


From the above output, notice that:
- There are 3 new format strings: %Z (frozenset), %b (bytes), %y (bytearray).
- These have 3 new identifier symbols: ⦓'frozenset'⦔, ‘bytes’, “bytearray”.
- The set and frozenset datatypes can both be printed with a %S or %Z.
- The bytes and bytearray datatypes can both be printed with a %b or %y.
- Any other type conversion raises a TypeError with a message like the one
  shown above. Notice that the error message says it crashed in printf.
  (In the above error output, I blanked out (____) some parts because they will
   be different for different students' implementations.)

Some other requirements exist that aren't seen in the above output. They are:
- You must raise a SyntaxError for all errors that aren't about types. Your
  error messages must describe what the error is.
- You must make all of the error messages that occur inside of printf to appear
  to crash in printf. What this means is: Suppose printf calls another function
  and it crashes in that other function -- then the error message must not
  mention that other function.
- You must allow the 3 new data types to work correctly with %a.
- You must modify the testSpecials.py function to not crash on the bad printf()
  tests. Instead, it should print the error message and continue. (So you will
  generate all of the error messages.) (You must also remember to modify that
  file's first line to import from PyPA4, not PyPA3.)
  - It is this requirement to not crash that is why you have to submit your
    modified version of testSpecials.py, in addition to the PyPA4.py file.


Notes:
- The tests in testnewtypes.py are only basic tests. When we do the grading,
  we will test many other cases as well.
- I didn't give you the testnewtypes.py file, but you can cut and paste it
  from above.
- I didn't give you the unicode values of the new new data types' symbols,
  but you can cut and paste them from above.
- I will post my solution to the previous assignment. You are free to use it
  as a starting point for this new assignment.
