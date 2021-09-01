# WAP of natural number from 1 to 10=55

a = 0
for x in range(1, 11):
    a = a + x

print("Sum of first 10 Natural Numbers is:", a)

# WAP to cal factorial of any number 5!=120

num = 5
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# WAP to cal fibonacci series 0 1 1 2 3 5 8 13

n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

# WAP for LCM, HCF, GCD
print("\n")
print("Enter Two Numbers for lcm: ")
numone = int(input())
numtwo = int(input())

if numone>numtwo:
    lcm = numone
else:
    lcm = numtwo

while True:
    if lcm%numone==0 and lcm%numtwo==0:
        break
    else:
        lcm = lcm + 1

print("\nLCM =", lcm)

# WAP for HCF

print("Enter Two Numbers for hcf: ", end="")
no = int(input())
nt = int(input())

if no>nt:
    hcf = no
else:
    hcf = nt

while True:
    if no%hcf==0 and nt%hcf==0:
        break
    else:
        hcf = hcf - 1

print("\nHCF (" + str(no) + ", " + str(nt) + ") = ", hcf)

# WAP to leap year

print("Calculating leap year")
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

# WAP to find armstrong number

num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# WAP to find palindrome number

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
# ENter five integer number and find max number(using simple if)

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))
num5 = int(input("Enter the fifth number:"))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("Maximum number :" , num1)

elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("Maximum number :" , num2)

elif num3 > num1 and num3 > 2 and num3 > num4 and num3 > num5:
    print("Maximum number :" , num2)

elif num4 > num1 and num4 > num2 and num4 > num3 and num2 > num5:
    print("Maximum number :" , num4)

else:
    print("Maximum number : ", num5)

# ENter five integer number and find min number(using simple if)

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))
num5 = int(input("Enter the fifth number:"))

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print("Minimum number :" , num1)

elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    print("Minimum number :" , num2)

elif num3 < num1 and num3 < 2 and num3 < num4 and num3 < num5:
    print("Minimum number :" , num3)

elif num4 < num1 and num4 < num2 and num4 < num3 and num2 < num5:
    print("Minimum number :" , num4)

else:
    print("Minimum number : ", num5)

#ASCII