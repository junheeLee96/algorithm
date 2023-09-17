# 10868번 최솟값
from math import *
import sys

# 세그먼트 트리 초기화
def init(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree_min[node]

# 최솟값 쿼리
def query(node, start, end, left, right):
    if start > right or end < left:
        return 1000000001

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

# 세그먼트 트리 사이즈 계산
h = int(ceil(log2(n)))       # 트리의 높이
t_size = 1 << (h+1)     # 대략의 트리 총 노드 개수

arr = []
tree_min = [0] * t_size     # 최솟값 저장

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

init(1,0,n-1)

for _ in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]

    # 주어지는 a, b는 index가 아니라 번째수임을 주의해야함.
    print(query(1, 0, n-1, a-1, b-1))