n = int(input())
c = sorted(list(map(int, input().split())), reverse=True)
f = sorted(list(map(int, input().split())))
print(sum(c[i] * f[i] for i in range(n)) * 1000)
