from functools import lru_cache

@lru_cache(maxsize=None)
def a(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 2*a(n//2)
    else:
        return a(n//2) -3*a(n//2 + 1)


total = 0
bound = int(input("Enter the upper bound"))
for i in range(1, bound):
    total += a(i)
    if i%(bound/100) == 0:
        print((i/bound)*100)
print(f"S({bound}) = {total}")