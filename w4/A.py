n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = sorted(a)
m, d = 1, 1
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        d = a[i]
    elif a[i] + 2 == a[i + 1]:
        m = a[i] + 1
print(m)
print(d)
