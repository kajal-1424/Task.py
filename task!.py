def p1(N):
    for r in range(1, N+1):
        for c in range(1, r+1):
            print("*", end=" ")
        print()

p1(5)

#prime number check

def primecheck(num):
    c = 0
    for r in range(1, num + 1):
        if num % r == 0:
            c = c + 1

    if c == 2:
        print("prime number")
    else:
        print("not a prime number")

primecheck(7)

#print table
def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)

table(15)