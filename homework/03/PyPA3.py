# B073040047
numType = {int: "i", float: "f", complex: "j"}
otherType = {"s": str, "L": list, "T": tuple, "S": set, "D": dict, "B": bool}

def doIfMatches(A, B):
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
    declare_type = otherType[B[-1]]
    if(declare_type != type(A)):
        print("The format string is not match to the type of arg.")
        exit()

    # the declare type is match to the type!
    A = str(A)
    if(declare_type == dict):
        A = "«" + A[1:-1] + "»"
    elif(declare_type == tuple and A[-2] == ','):
        A = A.replace(',', "")
    elif(declare_type == set and not A):
        A = "{}"

    B = B[:-1] + "s"
    print(B % A, end='')

def putfORi(S): return ((S.find('.') != -1) and (S[:-1] + 'f')) or (S[:-1] + 'i')

def handleNumbers(A, B):
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
    if (B[-1] == 'j'):
        B = putfORi(B)
        if (B.find('+') != -1):
            print(((B if A.real < 0 else "%" + B[2:]) + "+" +
                   (B if A.imag < 0 else "%" + B[2:]))
                  % (A.real, A.imag), end='j')
        elif(A.real):
            print((B + "+" + B) % (A.real, A.imag), end='j')
        else:
            print(B % A.imag, end='j')
    else:
        print(B % A, end='')

def fprint(__1__, *__2__, __3__=[0]):
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
    def find_type(_type):
        result = None
        for key in otherType:
            if (otherType[key] == _type):
                result = key
                break
        return result

    if(__1__ == '*'):
        __3__[0] = 1
    elif (len(__2__) > __3__[0]):  # not finish args
        if(__1__ == "?"):
            print("Format string is finished, but the argument list is not completed.")
            exit()
        else:
            # normal print
            other = [otherType[i] for i in otherType]
            fmt = __1__
            me = __2__[__3__[0]]
            if(fmt[-1] == 'a'):
                if(type(me) in numType):
                    me = str(me)
                if(type(me) in other):
                        # always can find a type, because type(me) in other
                    fmt = fmt[:-1] + find_type(type(me))
                else:
                    print("Unsuppot type of me.")
                    exit()
            if(type(me) in numType):
                handleNumbers(me, fmt)
            else:
                doIfMatches(me, fmt)
            __3__[0] += 1
    elif (__1__ != "?"):
        print("The argument list is finished, but there is a new format string.")
        exit()
    else:
        # is end of args and __1__ is '?'
        __3__ = [0]

def printf(*__1__):
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
    if(len(__1__) == 0):
        pass
    else:
        fmt_str = __1__[0]
        import re
        i = 0
        fprint("*")
        while i < len(fmt_str):
            if (fmt_str[i] == "%"):
                # special produce "%%"
                pp = re.search(r"^%%", fmt_str[i:])
                if(pp and pp.start() == 0):
                    print("%", end='')
                    i += 2
                    continue
                # find the first alpha pass to fprint
                match = re.search("[aifjsLTSDB]", fmt_str[i:])
                if(match != None):
                    length = match.start() + 1
                    sub_fmt_str = fmt_str[i:i + length]
                    # print(sub_fmt_str)
                    i += length
                    fprint(sub_fmt_str, *__1__)
                else:
                    print(fmt_str[i:], end='')  # print all until the end
                    i = len(fmt_str)
                    break
            else:
                print(fmt_str[i], end='')  # print something not format sting
                i += 1
        fprint("?")

if __name__ == "__main__":
    from testNums import *
    from testTypes import *
    from testAny import *
    from testSpecials import *
    testNums()
    testTypes()
    testAny()
    testSpecials()
