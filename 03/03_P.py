# 03_P1
n = int(input())
ans = 1
for i in range(1, n+1) :
    ans *= i
print(ans)

# 03_P1 (Adv: recursive function)
def f(n) :
    return 1 if n < 2 else n * f(n-1)
print(f(int(input())))

# 03_P2 (Adv: recursive function)
def f(n) :
    return 1 if n < 2 else n * f(n-1)
n, r, t = [int(x) for x in input().split()]
if t == 1 :
    print(f(n) // f(n-r))
else :
    print(f(n) // (f(n-r) * f(r)))

# 03_P3
n = int(input())
ans = 0
for i in range(1, n) :
    if i % 3 == 0 or i % 5 == 0 :
        ans += i
print(ans)

# 03_P4
n = int(input())
ans = 0
for _ in range(n) :
    ans += float(input())
print('No Data' if n == 0 else ans / n)

# 03_P5
ans = 0
n = 0
while True :
    tmp = float(input())
    if tmp < 0 :
        print('No Data' if n == 0 else ans / n)
        break
    else :
        ans += tmp
        n += 1

# 03_P6 (Adv: list + next() + generator)
score = [0, 50, 55, 60, 65, 70, 75, 80, 100]
grade = ['Error', 'F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
while True :
    x = int(input())
    if x < 0 :
        break
    print( next((gr for sc, gr in zip(score, grade) if x < sc or x == sc == 100), 'Error') )

# 03_P7
n, x = [int(e) for e in input().split()]
cnt = 0
for _ in range(n) :
    t = int(input())
    if x == t :
        cnt += 1
print(cnt)

# 03_P8
n = int(input())
mx = 0
for a in range(1, n) :
    for b in range(a, n) :
        if a + b >= n :
            break
        if a**2 + b**2 == (n-a-b)**2 :
            mx = max(mx, n-a-b)
print(mx)

# 03_P9
a, b, c, xi, d = [float(e) for e in input().split()]
n = 1
while True :
    xf = xi - (a*(xi**2) + b*xi + c) / (2*a*xi + b)
    if abs(xf - xi) <= d :
        print(n)
        break
    n += 1
    xi = xf
    
# 03_P10 (Adv: list)
n = int(input())
ans = []
for i in range(n-1, 1, -1) :
    if n % i == 0 :
        ans += [i]
if len(ans) == 0 :
    print('Prime Number')
else :
    print(*ans)

# 03_P10 (Adv: list comprehension)
n = int(input())
ls = [x for x in range(n-1, 1, -1) if n % x == 0]
print(*ls if len(ls) > 0 else 'Prime Number')

# 03_P11
n = int(input())
p = [2]
if n < 0 :
    print('input unavailable')
elif n < 2 :
    print('none')
else :
    for i in range(3, n+1, 2) :
        for j in range(2, i) :
            if i % j == 0 :
                break
            if j == i-1 :
               p.append(i)
    print(*p)

# 03_P11 (Adv: set comprehension + Sieve of Eratosthenes)
from math import sqrt, ceil
n = int(input())
np = {j for i in range(2, int(ceil(sqrt(n)))) for j in range(2*i, n+1, i)}
p = [x for x in range(2, n+1) if x not in np]
if n < 0 :
    print('input unavailable')
else :
    print(*p if len(p) > 0 else 'none')