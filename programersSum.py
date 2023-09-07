sequence = [1, 1, 1, 2, 3, 4, 5]
k = 7

def solution(sequence, k):
    answer = []
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]
    for i in range(len(sequence)):
        if sum(sequence[0:i]) <= k and sum(sequence[len(sequence)-i:]) >= k:
            for j in range(len(sequence)-i):
                if k == sum(sequence[j:j+i]):
                    answer = [j, j + i - 1]
                    break
        if answer: break
    return answer

print(solution(sequence, k))
