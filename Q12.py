# Use a while loop to reverse a given number (e.g., 123 → 321).

# whiout while loop
a=123

print(int(str(a)[::-1]))

#with while loop
num=123
r=0

while num>0:
    D=num%10
    r=r*10+D
    num=num//10

print(r)