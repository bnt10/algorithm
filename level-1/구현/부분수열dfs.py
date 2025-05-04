"""
1부터 N 까지의 수가 주어질 때
이 중 일부를 선택해서 만든 수열 중에서
모든  부분 수열의 합이 정확히 S가 되는 경우의 수를 구하시오.


"""
N = 5
arr = [-7, -3, -2, 5, 8]
targetSum = 0

def dfs(index, total, selected):
    if index == N:
        if total == targetSum and selected > 0:
            return 1
        else:
            return 0

    pick = dfs(index + 1, total + arr[index], selected + 1)
    no_pick = dfs(index + 1, total, selected)

    return pick + no_pick

result = dfs(0, 0, 0)
print(result)


def dfss(index, total, selected):
    if index == N:
        if total == targetSum and selected > 0:
            return 1
        else:
            return 0

    pick = dfs(index + 1 , total + arr[index], selected +1)
    no_pick =dfs(index +1 , total, selected)
result = dfss(0,0,0)