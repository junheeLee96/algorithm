import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))


seg_tree = [0 for _ in range(n * 4)]


def build_tree(x, left, right):
    if left == right:
        seg_tree[x] = arr[left]
        return seg_tree[x]

    mid = (left + right) // 2

    left_v = build_tree(x * 2, left, mid)
    right_v = build_tree(x * 2 + 1, mid + 1, right)

    seg_tree[x] = left_v + right_v
    return seg_tree[x]


build_tree(1, 0, n-1)


def find_tree(a, b, x, left, right):
    if a > right or b < left:
        return 0

    if a <= left and right <= b:
        return seg_tree[x]

    mid = (left + right) // 2

    left_v = find_tree(a, b, x * 2, left, mid)
    right_v = find_tree(a, b, x * 2 + 1, mid + 1, right)

    return left_v + right_v


answer = []
for _ in range(m):
    i, j = map(int, input().split())

    s = find_tree(i-1, j-1, 1, 0, n-1)
    print(s)

# print(answer)
