from math import ceil
Test_Case=int(input())
for i in range(0,Test_Case):
    X=int(input())
    Divided_Num=X/3
    Divided_Num=ceil(Divided_Num)
    Divided_Num*=3
    print(Divided_Num-X)
