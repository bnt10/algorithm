def solution(phone_book):
    S = set(phone_book)
    print(S)
    for num in phone_book:

        for i in range(1, len(num)):

            if num[:i] in S:
                print(num[:i])
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))