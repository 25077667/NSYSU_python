                             Programming in Python
                           Programming Assignment #3

Due date: Tuesday, May 5, at 11:59pm. (Start early, the assignment is hard)

Submission rules: Submit one file, named "PyPA3.py". The first line of your
                  file must be a comment that is exactly only your student ID

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
In this assignment, we will implement our own printf() function in Python.
In the C programming language, the printf function is a formatted print, with
a behavior rather similar to Python's % operator for strings:
% cat test.c
% cat pay.c
#include <stdio.h>
int main(){
    printf("%s worked %i hours at $%.2f/hour (=$%.2f).\n","Bob",8,90.0,8*90.0);
}
% gcc -o pay.x pay.c; ./pay.x
Bob worked 8 hours at $90.00/hour (=$720.00).
% cat pay.py
print("%s worked %i hours at $%.2f/hour (=$%.2f)."%("Bob",8,90.0,8*90.0))
% python3 pay.py
Bob worked 8 hours at $90.00/hour (=$720.00).
%

In the above, you can see how similar they are. But you can also see the differences:
 - print() ends with a \n, by default, but printf() requires you to say "\n".
 - % takes a format string on the left-side and a tuple on the right-side,
   but printf() takes a variable number of arguments.

Of course there are also some further differences that the above example
doesn't show. For example, C does not have a dictionary data type, so it
also doesn't have a format string for this data type.

Our implementation of printf() will have some features that make it different
than either C's printf("...",...) or Python's print("..."%(...)).

Our allowed format types are: integer (%i), float (%f), complex (%j), string (%s), boolean (%B), list (%L), tuple (%T), set (%S), dictionary (%D), and any (%a). I will not test how it behaves on other characters that Python's % operator allows (such as %d), but I will test that it fails on characters that the % operator doesn't allow (such as %Q).

In discussing these format types, I have created 3 other files for you to read. 
Look at README.testnums.txt first, and then look at README.testothers.txt.
Once you understand the assignment, then look at README.implementation.txt for 
coding instructions and hints.
