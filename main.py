def hi():
    print('hello world')


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def rotate(matrix):
    l = len(matrix)
    l_m = (l) // 2
    # TODO
    for i in range(l):
        for j in range(i, l):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(l):
        for c in range(l_m):
            temp = matrix[i][c]
            matrix[i][c] = matrix[i][-(c+1)]
            matrix[i][-(c+1)] = temp

    return matrix


