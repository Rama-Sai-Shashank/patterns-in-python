r=int(input("rows: "))
c=int(input("enter no of columns "))
print("Opp Right angle triangle")
for i in range(r+1):                            
    for j in range(r-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

print("Reverserightopp triangle")
for i in range(r):
    for j in range(i):
        print(' ',end=' ')
    for j in range(r-i):
        print('*',end=' ')
    print()

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

#r=int(input("rows: "))
print("Right angle triangle")
for i in range(r+1):
    for j in range(i):
        print('*',end=' ')
    print()

# *
# * *
# * * *
# * * * *
# * * * * *

print("Rev Right angle triangle")
for i in range(r+1):
    for j in range(r-i):
        print('*',end=' ')
    print()

# * * * * *
# * * * *
# * * *
# * *
# *

print("Square")
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print("Number Seq rev")
for i in range(r):
    for j in range(1,r+1-i):
        print(j,end=" ")
    print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

print("Number Seq")
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("Number")
for i in range(1,r+1):
    for j in range(i):
        print(i,end=" ")
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print("Number rev")
for i in range(1,r+1):
    for j in range(r-i+1):
        print(i,end=" ")
    print()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

print("Alphabet")
for i in range(1,r+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

# A
# B B
# C C C
# D D D D
# E E E E E

print('Number and star')
d=1
for i in range(r+1):
    for j in range(r-i):
        print(d,end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

# 1 1 1 1 1
# 1 1 1 1 *
# 1 1 1 * *
# 1 1 * * *
# 1 * * * *
# * * * * *

print("Number and numbers")
for i in range(r+1):
    for j in range(r-i):
        print(d,end=" ")
    for k in range(i):
        print(i,end=" ")
    print()

# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 2 2
# 1 1 3 3 3
# 1 4 4 4 4
# 5 5 5 5 5

for i in range(1,r+1):
    for j in range(r-i):
        print(i,end=" ")
    for k in range(i):
        print(d,end=" ")
    print()

# 1 1 1 1 1
# 2 2 2 1 1
# 3 3 1 1 1
# 4 1 1 1 1
# 1 1 1 1 1

print("Upper pyramid")
for i in range(r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range((2*i+1)):
        print("*",end=" ")
    print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

print("Lower pyramid")
for i in range(r):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*r-(2*i+1)):
        print("*",end=" ")
    print()

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

print("Square with gap")
for i in range(r):
    for j in range(r):
        if i==0 or j==0 or i==r-1 or j==r-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

print("Number sequence")
for i in range(1,r+1):
    num=i
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+r-j
    print()

# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

print("Alphabet seq")
for i in range(1,r+1):
    num=i
    ch=64
    for j in range(1,i+1):
        print(chr(ch+num),end=" ")
        num=num+r-j
    print()

# A
# B F
# C G J
# D H K M
# E I L N O

print("Alphabet side by side")
number = 65
for i in range(1, r + 1):
   for j in range(i):
     print(chr(number), end=" ")
     number += 1
   print()

# A
# B C
# D E F
# G H I J
# K L M N O

print("Number side by side")
number = 1
for i in range(1, r + 1):
   for j in range(i):
     print(number, end=" ")
     number += 1
   print()

# A
# B C
# D E F
# G H I J
# K L M N O

print("Square + symbol number seq")
mid = r // 2
for i in range(r):
    for j in range(r):
      row = abs(i - mid)
      col = abs(j - mid)
      print(max(r - row, r - col), end="") 
    print()

# 34543
# 44544
# 55555
# 44544
# 34543

print("Number square circle seq")
for i in range(r):
    for j in range(r):
      distance = min(i, j, r - i - 1, r - j - 1) 
      print(r - distance, end="") 
    print()

# 7777777
# 7666667
# 7655567
# 7654567
# 7655567
# 7666667
# 7777777