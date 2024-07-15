def solution(sticker):
    answer = 0
    if len(sticker) < 3:
        return max(sticker)
    sticker = [0, 0] + sticker

    # print(sticker)
    # print(len(sticker))

    dp = [0] * (len(sticker) + 2)
    dp2 = [0] * (len(sticker) + 2)
    for i in range(2, len(sticker)-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
        
    for i in range(3,len(sticker)):
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])


    return max(max(dp),max(dp2))



