# B073040047
numType = {int: "i", float: "f", complex: "j"}
otherType = {"s": str, "L": list, "T": tuple,
             "S": set, "D": dict, "B": bool, "b": bytes, "y": bytearray, "Z": frozenset}


def doIfMatches(A, B):
    """This checks if the datatype for object A matches to the format string B	
       (which means that it checks whether the last character of B indicates	
       the datatype of object A).	
       If they don't match, an error is printed and the program exits.	
       If they do match, then:	
        - A is converted to a string.	
        - If:	
           - its a dictionary, the {} symbols are converted to «» symbols.	
           - its a singleton tuple, the , is removed	
           - it an empty set, it becomes "{}"	
        - Then print the string, according to the format of B (but B's last	
          letter needs to first be converted to "s").                       """
    if B[-1] == 'S' and type(A) == frozenset:
        A = set(A)
    if B[-1] == 'Z' and type(A) == set:
        A = frozenset(A)
    if B[-1] == 'b' and type(A) == bytearray:
        A = bytes(A)
    if B[-1] == 'y' and type(A) == bytes:
        A = bytearray(A)

    if type(A) != otherType[B[-1]]:
        fmt_type = str(repr(otherType[B[-1]]))
        obj_type = str(type(A))
        raise TypeError("format string expects " + fmt_type[fmt_type.find("'") + 1: -2] +
                        " not " + obj_type[obj_type.find("'") + 1: -2])

    S = str(A)
    if B[-1] == 'D':
        S = "«"+S[1:-1]+"»"
    if B[-1] == 'S' and len(A) == 0:
        S = "{}"
    if B[-1] == 'T' and len(A) == 1:
        S = S[:-2]+")"
    if B[-1] == "b":
        S = "'" + S[S.find("'")+1: -1] + "'"
    if B[-1] == "y":
        S = '"' + S[S.find("'")+1: -2] + '"'
    if B[-1] == 'Z':
        S = "⦓" + S[S.find("{")+1:-2] + "⦔"
    print((B[:-1]+"s") % (S), end="")


def putfORi(S): return S[:-1]+("." in S and "f" or "i")


def handleNumbers(A, B):
    end = ""
    if B[-1] == "j":
        end = "j"
        B = putfORi(B)
        if '+' in B or complex(A).real:
            if '+' in B:
                B = "%"+B[2:]
            print(B % (complex(A).real), end="+")
        A = complex(A).imag
    print(B % (A), end=end)


def fprint(c, *v, pos=[0]):
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
    pos[0] += 1
    if c in "*?":
        if c == "?" and pos[0] < len(v):
            raise SyntaxError(
                "Error. Extra value arguments given:" + v[pos[0]:])
        pos[0] = 0
        return
    if pos[0] >= len(v):
        raise SyntaxError("Error. No value argument given for " + c + ".")
    me = v[pos[0]]
    if c[-1] == "a":
        if type(me) in numType:
            me = str(me)
        typpos = list(otherType.values()).index(type(me))
        c = c[:-1]+list(otherType.keys())[typpos]

    if type(me) in numType:
        handleNumbers(me, c)
    else:
        doIfMatches(me, c)


def printf(*v):
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
         - When finished, we need to call fprint() again with a "?" to ensure 	
           that there were no extra arguments.                              """

    if v == ():
        return 0
    if type(v[0]) != str:
        raise Exception("Error. No format string.")

    fprint("*")
    percent = False
    for c in v[0]:
        if percent:
            code = code+c
            if code == "%%":
                print("%", end="")
                percent = False
            elif c.isalpha():
                try:
                    fprint(code, *v)
                except (SyntaxError, TypeError, ValueError) as message:
                    print(message)
                    raise
                finally:
                    percent = False
        elif c == "%":
            percent = True
            code = c
        else:
            print(c, end="")
    else:
        if percent:
            raise Exception("Error. Incomplete format:", code)
        fprint("?", *v)


if __name__ == "__main__":
    from testNums import *
    from testTypes import *
    from testAny import *
    from testSpecials import *
    testNums()
    testTypes()
    testAny()
    testSpecials()
