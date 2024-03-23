
def solution(bandage, health, attacks):
    #
    max_health = health
    time = 0
    idx = 0
    heal_time = 0
    max_time = attacks[-1][0]
    while True:
        time += 1
        if time > max_time:
            answer = health
            break
        attack = attacks[idx]

        if time == attack[0]:
            health = health - attack[1]
            idx += 1
            heal_time = 0

            if health <= 0:
                answer = -1
                break

        else:
            health = health + bandage[1]
            heal_time += 1
            if heal_time == bandage[0]:
                heal_time = 0
                health += bandage[2]

            if health >= max_health:
                health = max_health
        # print(f'''
        #       time = {time}
        #       health = {health}
        #       heal_time = {heal_time}
        #       idx = {idx}
        #       ''')
    # answer = 0
    return answer