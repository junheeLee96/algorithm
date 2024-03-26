
def solution(b):
    o, x = sum([arr.count('O') for arr in b]), sum(
        [arr.count('X') for arr in b])
    if 0 <= o - x <= 1:
        rb = [b[0][i] + b[1][i] + b[2][i] for i in range(3)]
        winO, winX = 0, 0

        for i, j in zip(b, rb):
            if 'OOO' in [i, j]:
                winO += 1
            if 'XXX' in [i, j]:
                winX += 1

        dia = [b[0][0] + b[1][1] + b[2][2], b[0][2] + b[1][1] + b[2][0]]

        winO += dia.count('OOO')
        winX += dia.count('XXX')

        if winX and winO:
            return 0
        if winO and winX == 0 and o == x:
            return 0
        if winX and winO == 0 and o != x:
            return 0

        return 1
    else:
        return 0