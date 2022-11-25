#control flow statements

a = False

if a:
    print("the value is true")

a = 5

if a==3:   
    print("false")
elif(a==5):
    print("true")


# can profile A access profile B

# a = isfriend
# b = isblocked
# c = isadmin
# d = iszuckerberg


x =int(input())
y =int(input())
z =int(input())

if(z > y and z > x):
    print(z)

elif(x > y and x > z):
    print(x)
    
elif(y > x and y > z):
    print(y)

elif(x ==y and x ==z):
    print(x)

elif(x ==y and y>z):
    print(x)

elif(y ==z and z>x):
    print(y)

elif(x ==z and x>y):
    print(x)    

elif(x ==y and y<z):
    print(z)

elif(y ==z and z<x):
    print(x)

elif(x ==z and x<y):
    print(y)    