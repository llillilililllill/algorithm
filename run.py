players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]


def solution(players, callings):
    answer = []
    for i in callings:
        n = players.index(i)
        players[n], players[n-1] = players[n-1], players[n]
    answer = players
    return answer

print(solution(players, callings))