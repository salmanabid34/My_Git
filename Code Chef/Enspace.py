t=int(input())

for i in range(0,t):
    N,X,Y=map(int,input().split(" "))
    Y=Y*2
    if(N>=X+Y):
        print("yes")
    else:
        print("no")   
