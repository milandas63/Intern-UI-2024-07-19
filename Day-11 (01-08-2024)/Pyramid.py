# a) Pyramid of stars
spaces = 40
stars = 1
for i in range(0,10):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(0,stars):
        print("*",end="")
    print()
    spaces = spaces-1
    stars = stars+2

# b) Diamond of stars
print()
spaces = 40
stars = 1
for i in range(0,19):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(0,stars):
        print("*",end="")
    print()
    if i<9:
        spaces = spaces-1
        stars = stars+2
    else:
        spaces = spaces+1
        stars = stars-2

# c) Pyramid of Pallindrome numbers
print()
spaces = 40
for i in range(1,10):
    for j in range(1,spaces):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
    spaces = spaces-1

#   14 b) Print all PRIME NUMBERS between 2 given numbers?
print()
start = 1000
end = 3000
max_per_line = 15
count = 0
for i in range(start, end+1):
    yesno = True
    for j in range(2, i):
        if i%j==0:
            yesno = False
            break
    if yesno:
        print(i, end=" ")
        count = count+1
        if count>=max_per_line:
            print()
            count = 0
