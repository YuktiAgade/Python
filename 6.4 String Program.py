s = "Hello"
for ch in s:
    print(ch)

s = "Python"
print("String:", s)
print("First char:", s[0])
print("Last char:", s[-1])

s = "I love Python programming"
words = s.split()
for w in words:
    print(w, len(w))
s = "This is a simple program"
for w in s.split():
    if len(w) % 2 == 0:
        print(w)

s = "Hello World"
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

def display(name):
    print("Hello", name)

display("Suhani")

s = "Hi "
print(s * 3)
