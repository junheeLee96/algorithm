def solution(wallpaper):
    answer = []
    top = 99
    left = 99
    
    bottom = -1
    right = -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if top > i:
                    top = i
                    
                    
                if left > j:
                    left = j
                    
                if bottom < i:
                    bottom = i
                
                if right < j:
                    right = j
    
    # print(top,left,bottom,right)
    answer = [top,left,bottom+1,right+1]
                
    
    return answer