#WHILE

a = 1
while a<10:
    print(a)
    a+=1

#FOR

name = "asef"
name.__iter__
for c in name:
    print(c)

#BREAK, COUNTINUE ,PASS

for i in range(5):
    print(i)
    if i == 3:
        break

for i in range(5):
    print(i)
    i= 100
    print(i)

for i in [0,1,2,3,4]:
    print(i)
    i=100
    print(i)

for i in range(5):
    print(i)
else:
    print("something")
    
