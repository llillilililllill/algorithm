a = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

b = [[1, 4], [4, 5], [3, 7], [4, 8], [5, 12], [11, 13], [10, 14]]
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    target_in = 0

    for target in targets:
        if target_in <= target[0]:
            answer += 1
            target_in = target[1]

    return answer