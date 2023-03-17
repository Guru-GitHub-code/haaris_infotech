n = int(input())
s =n
for i in range(1,n+1):
    for j in range(s):
        print(" ",end="")
    for k in range(1,i+1):
        if(i%2==0):
            print("#",end=" ")
        else:
            print("*",end=" ")

    print("")
    s-=1