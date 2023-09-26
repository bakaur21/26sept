#problem1 
#convert decimal numbers to octal numbers 
d_num=int(input("Enter a decimal number"))
oct_num=oct(d_num)
print("The octal number for " + str(d_num)+ " is  "+str(oct_num))

#problem2 
#reverse an integer in python 
num=123456
rev_num=0
while(num>0):
    rem=num%10
    rev_num=(rev_num*10)+rem
    num=num//10
print("The Reversed Number is : "+str(rev_num))

#problem3 
#Print the Fibonacci series using the recursive method.
def rec(n):
    if(n<=1):
        return n
    else:
        return(rec(n-1)+rec(n-2))
terms=6
print("Fibonacci sequence ")
for i in range(terms):
    print(rec(i))

#problem4 
#Return the Nth value from the Fibonacci sequence
n=int(input("Please enter the nth value for fibonacci sequence "))
print("nfivuewhvfu")
def fibonacci(n):
    if(n<=0):
        print("please enter a valid input")
    elif(n==1):
        return 0 
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n))
