from itertools import combinations

arr = list(map(int, input().split()))

arr.sort()

# t = arr[:3]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def find_lcm(numbers):
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])
    return lcm_result


result = 1000000
for i in combinations(arr, 3):
    a = find_lcm(i)
    if a < result:
        result = a

print(result)
