def solution(answers):
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    std1_repeated = [std1[i % len(std1)] for i in range(len(answers))]
    std2_repeated = [std2[i % len(std2)] for i in range(len(answers))]
    std3_repeated = [std3[i % len(std3)] for i in range(len(answers))]

    result = [0, 0, 0]

    for idx, ans in enumerate(answers):
        if std1_repeated[idx] == ans:
            result[0] += 1
        if std2_repeated[idx] == ans:
            result[1] += 1
        if std3_repeated[idx] == ans:
            result[2] += 1

    max_score = max(result)
    answer = [i + 1 for i, score in enumerate(result) if score == max_score]
    
    return answer