n = 5

for i in range(n):
    for j in range(n):
        print(i,end= " ")
    print()

n = 5
for i in range(n):
    for j in range(n):
            print(n-j,end=" ")
    print()

    n = 5
for i in range(n):
    for j in range(n):
            print(max(i,j),end=" ")
    print() 

    n = 5
for i in range(n):
    for j in range(n):
            print(max(i,j),max(n-j-1 , n-i-1),end=" ")
    print() 

print(max(1,2,3,4,5,6,7,8,9))