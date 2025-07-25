# a= int(input("Enter the first number"))
# b= int(input("Enter the second number"))
# sum = a+b
# print (sum)
# wap to calculate factorial of a number
n = int(input("enter the number"))

fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)