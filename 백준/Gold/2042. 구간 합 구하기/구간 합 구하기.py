import sys
input = sys.stdin.readline

# 수의 개수, 수 변경 횟수, 구간의 합 횟수
n,m,k = map(int,input().split())
num = [int(input()) for _ in range(n)]

# 세그먼트 트리
# seg_tree[1] : 모든 노드의 합
# seg_tree[2] : 0~n//2번 노드의 합
# seg_tree[3] : n//2+1~n번 노드의 합
seg_tree = [0 for _ in range(4*n)]

# 1. 세그먼트 트리 만들기
# seg_tree[x] 값 구하기
def build_tree(x,left,right):
    if left == right:
        seg_tree[x] = num[left]
        return seg_tree[x]
    mid = (left + right)//2
    left_value = build_tree(2*x,left,mid)
    right_value = build_tree(2*x+1,mid+1,right)
    seg_tree[x] = left_value + right_value
    return seg_tree[x]

build_tree(1,0,n-1)

# 2. 세그먼트 트리로 구간 합 구하기
# b~c구간합 구하기
# 트리의 구간 left~right
# 현재 노드 x
def find_tree(b,c,x,left,right):
    # 구하고 싶은 구간(b~c)가 현재 트리 구간에 포함 X
    if c < left or right < b:
        return 0
    # 구하고 싶은 구간(b~c) 안에 현재 트리 포함
    if b <= left and right <=c:
        return seg_tree[x]
    # 구간이 겹치는 경우
    mid = (left + right)//2
    left_value = find_tree(b,c,x*2,left,mid)
    right_value = find_tree(b,c,x*2+1,mid+1,right)
    return left_value + right_value

# 3. 세그먼트 트리 값 업데이트
# 인덱스 idx의 값을 val로 바꾸기
def update_tree(x,left,right,idx,val):
    # 길이 1인 구간
    if left == right == idx:
        seg_tree[x] = val
        return
    # 현재 구간에 idx가 포함 X
    if idx < left or right < idx:
        return
    
    mid = (left + right)//2
    # 왼쪽 자식 업데이트
    update_tree(x*2,left,mid,idx,val)
    # 오른쪽 자식 업데이트
    update_tree(x*2+1,mid+1,right,idx,val)
    
    # 업데이트 된 자식 노드를 통해 현재 노드 업데이트
    seg_tree[x] = seg_tree[x*2] + seg_tree[x*2+1]
    
for _ in range(m+k):
    a,b,c = map(int,input().split())
    # b번째 수를 c로 바꾸기
    if a == 1:
        update_tree(1,0,n-1,b-1,c)
    # b번째 수부터 c번째 수까지 합 구하기
    else:
        s = find_tree(b-1,c-1,1,0,n-1)
        print(s)