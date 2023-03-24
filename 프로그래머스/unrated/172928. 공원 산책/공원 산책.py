def solution(park, routes):
    answer = [0,0]
    
    for i in range(len(park)):
        idx = park[i].find('S')
        if idx != -1:
            answer[0] = i
            answer[1] = idx
            break

    for i in range(len(routes)):
        direction, count = routes[i].split(' ')
        Wall = False
        count = int(count)
        position = answer[:]
        Wall = False
        for j in range(count):
            if direction == 'N':
                if  (0 <= position[0] - 1 < len(park)):
                    if park[position[0] - 1][position[1]] != 'X':
                        position[0] -= 1
                    else:
                        Wall = True
                        break
                else:
                        Wall = True
                        break
                        
            if direction == 'S':
                if  (0 <= position[0] + 1 < len(park)):
                    if park[position[0] + 1][position[1]] != 'X':
                        position[0] += 1
                    else:
                        Wall = True
                        break
                else:
                        Wall = True
                        break
                        
            if direction == 'W':
                if ( 0 <= position[1] - 1 < len(park[0]) ):
                    if park[position[0]][position[1] - 1] != 'X':
                        position[1] -= 1
                    else:
                        Wall = True
                        break
                else:
                        Wall = True
                        break
                        
            if direction == 'E':
                if  ( 0 <= position[1] + 1 < len(park[0])):
                
                    if park[position[0]][position[1] + 1] != 'X':
                        position[1] += 1
                    else:
                        Wall = True
                        break
                else:
                        Wall = True
                        break
                    
        if Wall == False:
            answer = position[:]
        
    return answer

