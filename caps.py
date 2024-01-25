a = [1, 2]
c = 0
for i in range(3, 1000):
    for j in range(2, i-1):
        if i % j == 0:
            c += 1
    if c == 0:
        a.append(i)
    c = 0
b = int(input("enter the number of terms: "))
for i in range(0, b-1):
    print(a[i], end="  ")