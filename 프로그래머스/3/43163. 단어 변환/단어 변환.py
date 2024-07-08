from collections import deque
from copy import deepcopy


def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append([begin, 0])

    while q:
        s, cnt = q.popleft()

        if s == target:
            return cnt

        # s = list(s.strip())

        new_words = deepcopy(words)

        for i in range(len(words)):
            isnt_same_cnt = 0
            for j in range(len(words[0])):
                if s[j] != words[i][j]:
                    isnt_same_cnt += 1
                    # return

            if isnt_same_cnt == 1:
                q.append([words[i], cnt + 1])
                new_words.remove(words[i])

        words = new_words

    return 0