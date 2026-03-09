s = "Hello"
s += " World"
print(s)

a = "Hello"
b = "Python"
c = a + " " + b
print(c)

s = "Python Programming"
print("Python" in s)

s = "\x48\x65\x6c\x6c\x6f"
print(s)

name = "Suhani"
print(f'"{name}"')

print(r"Hello\nWorld")

s = "abc"
n = len(s)
print(n*(n+1)//2)

s = "Python"

# 1
print(s[::-1])

# 2
print("".join(reversed(s)))

# 3
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 4
print("".join(list(s)[::-1]))

# 5
def reverse(x):
    if len(x)==0:
        return x
    return reverse(x[1:]) + x[0]
print(reverse(s))
