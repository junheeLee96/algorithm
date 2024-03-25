

def solution(data, ext, val_ext, sort_by):
    answer = []

    arr = ['code', 'date', 'maximum', 'remain']
    idx = arr.index(ext)
    sort_idx = arr.index(sort_by)
    for i in data:
        info = i

        if val_ext > info[idx]:
            answer.append(info)

    answer = sorted(answer, key=lambda x: x[sort_idx])

    return answer
