//1
12
123
1234
12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

//1
22
333
4444
55555

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

//1
21
321
4321
54321

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

//1
10
101
1010
10101

for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("1", end="")
        else:
            print("0", end="")
    print()

//2
4 6
8 10 12
14 16 18 20

num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
