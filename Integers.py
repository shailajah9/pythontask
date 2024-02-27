###Integer ,Float,Complex
#int are zero,postive or negative whole numbers denots by int
#leading zero in nonzero numbers is not valitd in python ,ex 009567

#examples 
a = 55
print("type of a : ",type(a))

a = 34
print(type(a))

X = 34
Y = 44
C = X+Y
print(C)
print("type of C : ",type(C))
U=X-Y
print(U)
print("type of U : ",type(U))
O=X//Y
print(O) 
print("type of O : ",type(O))
H=X/Y
print(H)
print("type of H : ",type(H))
S=X*Y
print(S)
print("type of S : ",type(S))
K=X**Y
print(K)
print("type of K : ",type(K))

#The int() function converts a string or float to int.

x = '100'
print(x) 
print("type of x : ",type(x))

#likewise 
y = int('-10')
print(y) 
print("type of y : ",type(y))

z = 5.5
print(z) 
print("type of z : ",type(z))

n = '100', 2
print(n) 
print("type of n : ",type(n))


##Integers can be binary, octal, and hexadecimal values

#binary
#A number having 0b with eight digits in the combination of 0 and 1 represent the binary numbers in Python. For example, 0b11011000 is a binary number equivalent to integer 216.
x = 0b11011000
print(x)

x = 0b_1101_1000
print(x)
print(type(x))

#octal
#A number having 0o or 0O as prefix represents an octal number. For example, 0O12 is equivalent to integer 10.
x = 0o12

print(x)
print(type(x))

#hexadecimal
#A number with 0x or 0X as prefix represents hexadecimal number. For example, 0x12 is equivalent to integer 18.
x = 0x12

print(x)
print(type(x))


a,b = 20,40
print(a+b) #addition
print(a-b) #subration
print(a*b) #multiplcation
print(b/a) #Division


a=3
print(a**2) #exponetial
print(a**3) 

a,b = 9, 2
print(a//b)#Floor division(reminder)


####user define input 
x= (input ("the value of x = "))
y= (input ("the value of y = "))


a = (input ("the value of a = "))
print(type(a))


X = (input ("the value of X = "))
Y = (input ("the value of Y = "))
C = X+Y
U =X-Y
O=X//Y
H=X/Y
S=X*Y
K=X**Y
print(C,U,H,S,K)
print("type of C : ",type(C))
