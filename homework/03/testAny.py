from PyPA3 import *
def testAny():
    print('printf("%a,%+10a,%-10a,%010a\\n","1","2","3","4.5"):')
    print("√ = 1,         2,3         ,       4.5\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n","1","2","3","4.5")

    print('\nprintf("%a,%+10a,%-10a,%010a\\n",[1],[2],[],[4,5]):')
    print("√ = [1],       [2],[]        ,     [4.5]\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n",[1],[2],[],[4.5])
    
    print('\nprintf("%a,%+10a,%-10a,%010a\\n",(1,),(2,),(),(4,5)):')
    print("√ = (1),       (2),()        ,    (4, 5)\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n",(1,),(2,),(),(4,5))

    print('\nprintf("%a,%+10a,%-10a,%010a\\n",{1:1},{2:2},{},{4:4,5:5}):')
    print("√ = «1: 1»,    «2: 2»,«»        ,«4: 4, 5: 5»\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n",{1:1},{2:2},{},{4:4,5:5})

    print('\nprintf("%a,%+10a,%-10a,%010a\\n",True,True,False,False):')
    print("√ = True,      True,False     ,     False\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n",True,True,False,False)
    
    print('\nprintf("%a,%+10a,%-10a,%010a\\n",1,2,.3,.4):')
    print("√ = 1,         2,0.3       ,       0.4\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n",1,2,.3,.4)
    
    print('\nprintf("%a,%+10a,%-10a,%010a\\n",1j,2j,.3j,.4j):')
    print("√ = 1j,        2j,0.3j      ,      0.4j\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n",1j,2j,.3j,.4j)
    
    print('\nprintf("%a,%+10a,%-10a,%010a\\n",1+1j,2+2j,3+.3j,.4+4j):')
    print("√ = (1+1j),    (2+2j),(3+0.3j)  ,  (0.4+4j)\n? = ",end="")
    printf("%a,%+10a,%-10a,%010a\n\n",1+1j,2+2j,3+.3j,.4+4j)

if (__name__=="__main__"):
    testAny()
