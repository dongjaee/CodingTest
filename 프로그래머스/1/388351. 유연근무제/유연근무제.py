def solution(schedules, timelogs, startday):
    answer = 0
    dream = [a + 10 if a % 100 < 50 else a + 50 for a in schedules]

    for i in range(len(timelogs)):  
        s = startday - 1  
        valid = True  

        for j in range(7):  
            s = (s % 7) + 1  

            if s % 6 == 0 or s % 7 == 0: 
                continue

            if timelogs[i][j] > dream[i]: 
                valid = False
                break 
        
        if valid:
            answer += 1  

    return answer