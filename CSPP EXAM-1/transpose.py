def transpose(matrix):
    if len(matrix)==0:
        return []
    transpose = []
    for i in range(len(matrix[0])):
        l = []
        for j in range(len(matrix)):
            l.append(matrix[j][i])
        transpose.append(l)
    print(transpose)
    return transpose
        





# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
assert transpose([[1]]) == [[1]]
assert transpose([]) == []
assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
assert transpose([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
assert transpose([['a', 'b'], ['c', 'd'], ['e', 'f']]) == [['a', 'c', 'e'], ['b', 'd', 'f']]

print("All tests passed!")
