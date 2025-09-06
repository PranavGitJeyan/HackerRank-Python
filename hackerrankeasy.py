#1Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20 , print Not Weird
n=int(input())
if n%2==0 and 2<=n<=5:
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")
else:
    print("Weird")

#or

n=int(input())
if n%2==0:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")

#2Task
#The provided code stub reads two integers a and b from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
a=int(input())
b=int(input())
if 1<=a<=10e10 and 1<=b<=10e10:
    print(a+b)
    print(a-b)
    print(a*b)
else:
    print()

#Task3
#The included code stub will read an integer n, , from STDIN.
#Without using any string methods, try to print the following:123...n
#Note that "" represents the consecutive values in between.
#Example n=5
#Print the string 12345.
#Print the list of integers from  through  as a string, without spaces.
#Sample Input 0
#3
#Sample Output 0
#123
n=int(input())
for i in range(1,n+1):
    if 1<=n<=150:
        print(i,end="")
    else:
        print()