name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    answer = [0] * len(photo)

    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                answer[i] += yearning[name.index(photo[i][j])]
    return answer

print(solution(name, yearning, photo))
