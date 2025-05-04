def solution(words):
    answer = []
    for s in words.split(" "):
        temp = [word for word in s.lower()]
        for i in range(len(temp)):
            if i % 2 == 0 :
                temp[i] = temp[i].upper()
        answer.append("".join(temp))

    return " ".join(answer)

print(solution(("scss dccsaz")))

