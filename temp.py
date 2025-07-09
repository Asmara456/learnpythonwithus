# type casting ------ means changing one data type into another to get answer according to user requirement
a=30
b=float(a)
print(b)
# we can convert all data types in the same way i am giving one more example also to explain better
c="89"
d=int(c)
print(d)
# same as for input function because input function returns string so we typecast 
w=input("enter a number")
print(type(w))
# so the input function always return  type string even the user enters the number of int data type so here we fix it like this
p=int(input("enter the number"))
print(type(p))

#now moving towards operators in python
# arithmetic operators 
e=34
f=22
print(e+f) # it simply performs addition between numbers 
print(e-f) # it performs subtraction between numbers 
print(e*f) # it performs multiplication between numbers
print(e/f) # it divdes numbers 
print(e%f) # it is modulus sign dividing the number and giving remainder as output
print(e//f) # it divides numbers and removing fraction part and giving whole number as an output 
print(e**f) # it consider 2nd number as a power 


# relational operator ---- campares two values and giving output as boolean values like true or false 
g=5<4 # less than operator
print(g)  
g=6>8 # greater than operator
print(g)
g=7<=6 # less than or equal too operator 
print(g)
g=10>=10 # greter than or equals too
print(g)
g=7==7 # euality check operator 
print(g)
g=7!=8 # non equal operator 
print(g)

# logical operator in python
m=67
n=73
o=64
print(m>n and m>o) # and operator returns true if both conditions are true otherwise false 
print(m>n or m>o) # or operator returns true if any single condition is true 
print (not(m>o)) # it reverse the output true into false and viceversa 

# assignment operator used to assign a value to a variable 
z=10  # assigning value to z
print(z)
z=12
z+=8  # assigning value and add
print(z)
z=8
z-=6  #assigning value and subtract 
print(z)
z=5
z*=7  # assigning value and multiply 
print(z)
z=8
z/=8   # assigning value and divide 
print(z)
z=6
z%=2 # assiging value and modulus means output  remainder 
print(z)
z=10
z**=2 # raise power actually 
print(z)


