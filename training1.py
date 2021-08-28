# WAP for ADD,mul,div,sub
# for addition
a = 20
b = 10
print(a+b)

# for multiplication
a = 20
b = 10
print(a*b)
# for division
a = 20
b = 10
print(a/b)

# for subtraction
a = 20
b = 10
print(a-b)

# WAP to calculate simple interest

P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
SI = (P * N * R)/100
print("Simple interest : {}".format(SI))

# WAP for swapping using third variable

# Take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# WAP for swapping without using third variable

int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))

print('Old value of int1 is {0} and int2 is {1}'.format(int1, int2))

int1 = int1 + int2
int2 = int1 - int2
int1 = int1 - int2

print('New value of int1 is {0} and int2 is {1}'.format(int1, int2))

# WAP to calculate gross salary from basic sal(HRA=30% , TA=40% , DA=20%)

sal = 40000.0
HRA = 0.3 * sal
TA = 0.4 * sal
DA = 0.2 * sal
gross = sal + HRA + TA + DA
print("Gross salary: ", gross)

# WAP to find circumference of circle

r = 6
pi = 3.14
C = 2*pi*r
print("Circumference: ", r)

# WAP to find area of circle

r = 6
pi = 3.14
area = pi *(r**2)
print("Area of Circle: ", area)

# WAP to reverse three number ex: 123 = 321

a = 123
revno = 0
while (a>0):
    remainder = a%10
    revno = (revno * 10) + remainder
    a = a // 10
print("Reverse number: ", revno)
# WAP to enter height of user in feets and convert it into inches and centimeter.

hf = 6
hi = hf * 12
hc = hi * 2.54
print("Height: ", hi, hc)

# WAP to take centigrade temp and convert it into feranite temp. f = 1.8*c+240

c = 32
f = 1.8*c +32
print("Temp: ", f)