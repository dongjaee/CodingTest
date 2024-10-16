def solution(park, routes):
    h = len(park)
    w = len(park[0])

    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    direction_map = {
        'N': (-1, 0),  
        'S': (1, 0),   
        'W': (0, -1), 
        'E': (0, 1)    
    }

    for route in routes:
        dir, dist = route.split()
        dist = int(dist)

        dx, dy = direction_map[dir]
        new_x, new_y = x, y
        valid = True

        for _ in range(dist):
            new_x += dx
            new_y += dy
            
            if not (0 <= new_x < h and 0 <= new_y < w) or park[new_x][new_y] == 'X':
                valid = False
                break

        if valid:
            x, y = new_x, new_y

    return [x, y]