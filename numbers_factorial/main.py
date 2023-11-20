# Factorial Using Loop
num = 15
st = 1

for x in range(st, num + 1):
    st *= x

print(f"Factorial of {num} is {st}")

# Factorial using recurssion

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
print(f"Factorial of number 5 is ",fact(5))