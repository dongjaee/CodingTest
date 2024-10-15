def get_divisors(n):
    divisors_count = 0
    for i in range(1, int(n ** 0.5) + 1): 
        if n % i == 0:
            divisors_count += 1  
            if i != n // i: 
                divisors_count += 1
    return divisors_count

def solution(number, limit, power):
    result=0
    for i in range(1,number+1):
        if get_divisors(i)>limit:
            result+=power
        else:
            result+=get_divisors(i)
                
    return result