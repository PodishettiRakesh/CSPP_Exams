def find_uniques(nums):
    # Placeholder for the actual function implementation
    dic={}
    ans=[]
    for each in nums:
        if each not in dic:
            dic[each]=1
        else:
            dic[each]+=1
    for key, value in dic.items():
        if value==1:
            ans.append(key)
    # print(ans)
    return ans


# Extensive testing of the function
if __name__ == "__main__":
    # These tests should fail initially as the function does not yet have an implementation.
    assert find_uniques([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5], "Test case 1 failed"
    assert find_uniques([7, 7, 7, 7]) == [], "Test case 2 failed"
    assert find_uniques([]) == [], "Test case 3 failed"
    assert find_uniques([2, 2, 3, 3, 4, 4, 4, 5]) == [5], "Test case 4 failed"
    assert find_uniques([10, 10, 11]) == [11], "Test case 5 failed"
    assert find_uniques([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 6 failed"
    assert find_uniques([100, 200, 300, 300, 200, 100, 400]) == [400], "Test case 7 failed"
    print("All testcases passed")
