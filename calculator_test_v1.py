print(" Welcome to the world of Maths ")

print("Please enter your name->")
user=input()
print(" Hello " +user)

print("Please select your option number to perform: \n1> Addition \n2> Subtraction \n3> Multiplication \n4> Division \n5> Number Root ")
select=input()

option=" "

def maths(x,y):
    n=2
    n1=0
    n2=0
    while n>0 :
        if x=='1':
            y="Addition"
            n3=n1+n2
        elif x=='2':
            n3=n1-n2
            y="Subtraction"
        elif x=='3':
            n3=n1*n2
            y="Multiplication"
        elif x=='4':
            n3=n1/n2
            y="Division"
        elif x=='5':
            n3=n1**n2
            y="Number Root"
        if n==1 : 
            n1=int(input())
            n2=int(input()) 
            print(n)
        else :
            print ("We are going to perform",y, ".\nPlease provide two numbers to perform ",y)
            print(n)
        n-=1   
    return(n3,y)

   
x = maths(select,option)

print("Output of ",x[1], "is :",x[0])
