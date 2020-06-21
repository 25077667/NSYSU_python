# B073040047
from PyPA5 import *
# frozenset converts to set
printf("Print as %%S: %S %S\n", {1, 2}, frozenset({3}))
# set converts to frozenset
printf("Print as %%Z: %Z %Z\n", {1, 2}, frozenset({3}))
printf("Print as %%s: %s\n", 'Hello')
printf("Print as %%b: %b %b\n", b'Hello', bytearray(b'Bye'))  # Convertable
printf("Print as %%y: %y %y\n", bytearray(b'Hello'), b'Bye')  # Convertable
printf("This will crash: %s\n", b'Hello')  # bytes aren't equal to strings
