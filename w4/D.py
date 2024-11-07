from heapq import heapify, heappop, heappush
from sys import exit

n = int(input())
if n == 1:
    print(int(input()))
    exit(0)

heap = [-1 * int(input()) for _ in range(n)]
heapify(heap)
while len(heap) > 1:
    e1, e2 = -1 * heappop(heap), -1 * heappop(heap)
    diff = max(e1, e2) - min(e1, e2)
    if diff != 0:
        heappush(heap, -1 * diff)
if len(heap) == 0:
    print("NONE")
else:
    print(-1 * heap[0])
