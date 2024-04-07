
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = 999999999999999999999999999999


t = int(input())


for _ in range(t):
    w = input().strip()
    k = int(input())

    char_dict = defaultdict(list)

    for idx, char in enumerate(w):
        if w.count(char) >= k:
            char_dict[char].append(idx)

    short = INF

    long = 0

    for char, idx_list in char_dict.items():
        if len(idx_list) == k:
            length = idx_list[-1] - idx_list[0] + 1
            if length < short:
                short = length
            if length > long:
                long = length

        elif len(idx_list) > k:
            st = 0

            while 1:
                nd = st + (k - 1)
                length = idx_list[nd] - idx_list[st] + 1

                if length < short:
                    short = length
                if length > long:
                    long = length

                if nd == (len(idx_list) - 1):
                    break

                st += 1

    if not long and short > 10000:
        print(-1)
    else:
        print(short, long)
