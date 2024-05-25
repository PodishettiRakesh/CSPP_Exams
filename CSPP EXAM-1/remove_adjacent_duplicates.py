def remove_adjacent_duplicates(s):
    if len(s)==0:
        return []
    original=[]
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            original.append(s[i])
    original.append(s[len(s)-1])

    print(original)  
    return original 




assert remove_adjacent_duplicates([1, 2, 2, 3, 3, 5, 3, 4]) == [1, 2, 3, 5, 3, 4]
assert remove_adjacent_duplicates([1, 1, 2, 3, 1, 5, 5, 5, 5, 6, 6]) == [1, 2, 3, 1, 5, 6]
assert remove_adjacent_duplicates([1, 1, 1, 1, 1, 1, 1]) == [1]
assert remove_adjacent_duplicates([]) == []
assert remove_adjacent_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_adjacent_duplicates([2, 2, 2, 3, 3, 2, 2]) == [2, 3, 2]
assert remove_adjacent_duplicates([-1, -1, 2, 2, -1, -1]) == [-1, 2, -1]
assert remove_adjacent_duplicates([7, 7, 3, 4, 4, 4]) == [7, 3, 4]
assert remove_adjacent_duplicates([10]) == [10]
assert remove_adjacent_duplicates([1000, 1000, 1000, 2000, 2000, 3000]) == [1000, 2000, 3000]

print("All tests passed!")
