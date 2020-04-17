from PyPA3 import *
def testTypes():
    print('printf("%s,%+10s,%-10s,%010s\\n","1","2","3","4.5"):')
    print("√ = 1,         2,3         ,       4.5\n? = ",end="")
    printf("%s,%+10s,%-10s,%010s\n","1","2","3","4.5")

    print('\nprintf("%L,%+10L,%-10L,%010L\\n",[1],[2],[],[4,5]):')
    print("√ = [1],       [2],[]        ,     [4.5]\n? = ",end="")
    printf("%L,%+10L,%-10L,%010L\n",[1],[2],[],[4.5])
    
    print('\nprintf("%T,%+10T,%-10T,%010T\\n",(1,),(2,),(),(4,5)):')
    print("√ = (1),       (2),()        ,    (4, 5)\n? = ",end="")
    printf("%T,%+10T,%-10T,%010T\n",(1,),(2,),(),(4,5))

    print('\nprintf("%D,%+10D,%-10D,%010D\\n",{1:1},{2:2},{},{4:4,5:5}):')
    print("√ = «1: 1»,    «2: 2»,«»        ,«4: 4, 5: 5»\n? = ",end="")
    printf("%D,%+10D,%-10D,%010D\n",{1:1},{2:2},{},{4:4,5:5})

    print('\nprintf("%B,%+10B,%-10B,%010B\\n",True,True,False,False):')
    print("√ = True,      True,False     ,     False\n? = ",end="")
    printf("%B,%+10B,%-10B,%010B\n\n",True,True,False,False)
    
if (__name__=="__main__"):
    testTypes()
