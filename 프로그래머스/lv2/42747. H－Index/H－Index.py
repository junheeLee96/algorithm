def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx , c in enumerate(citations):
        if idx >= c:
            return idx
    return len(citations)