# cook your dish here
Test_Case=int(input())
if(Test_Case>=1 and Test_Case<=1000):
    for i in range(0,Test_Case):
        A,B,C,D=map(int,input().split(" "))
        if(A>=1 and A<=10 and B>=1 and B<=10 and C>=1 and C<=10 and D>=1 and D<=10 ):
            if(A==C or B==D):
                print(2)
            else:
                print(1)
