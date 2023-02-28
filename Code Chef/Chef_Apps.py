# cook your dish here
Test_Case=int(input())
for i in range(0,Test_Case):
    S,X,Y,Z=map(int,input().split(" "))
    Memory_Used_1=S-X-Y
    Memory_Used_2=S-X
    Memory_Used_3=S-Y
    if(Memory_Used_1>=Z):
        print(0)
    elif(Memory_Used_2>=Z or Memory_Used_3>=Z):
        print(1)
    else:
        print(2)
