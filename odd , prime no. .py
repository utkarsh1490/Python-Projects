        #ODD NUMBER IN RANGE

x=int(input("Enter the initializing number = "))
y=int(input("Enter the last number = "))
for i in range(x,y+1):
    if(i%2!=0):
        print(i,"is odd number")

        #PRIME NUMBER

x=int(input("Enter the Number = "))
s=0
for i in range(0,x+1):
    for j in range(1,i+1):
        if(i%j==0):
            s+=1
    if(s==2):
        print(i,"is a prime number")
    s=0

        #PRIME NUMBER IN A RANGE

x=int(input("Enter the initializing number = "))
y=int(input("Enter the last number = "))
s=0
for i in range(x,y+1):
    for j in range(1,i+1):
        if(i%j==0):
            s+=1
    if(s==2):
        print(i,"is a prime number")
    s=0
