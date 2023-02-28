Test_Case=int(input())
for i in range(0,Test_Case):
    Marks1,Marks2=map(int,input().split(" "))
    if(Marks2>Marks1):
        print(Marks2)
    else:
        print(Marks1)
