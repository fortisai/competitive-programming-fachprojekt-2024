from heapq import heappop, heappush

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
sw = []
for i in range(k):
    heappush(sw, (-a[i], i))
print(-sw[0][0])
for i in range(n - k):
    heappush(sw, (-1 * a[i + k], i + k))
    while sw and sw[0][1] <= i:
        heappop(sw)
    print(-sw[0][0])
