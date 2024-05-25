def longest_consecutive(nums):
    if len(nums)==0:
        return 0
    nums.sort()
    original=1
    
    for i in range(len(nums)-1):
        count=1
        value=nums[i]
        for j in range(i+1,len(nums)):
            if nums[j]-value==1:
                value=nums[j]
                count+=1
                
        if count>original:
            original=count
    print(original)
    return original




# Extensive testing of the function
if __name__ == "__main__":
    # These tests will initially fail because the function does not yet have an implementation.
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4, "Test case 1 failed"
    assert longest_consecutive([1, 9, 3, 10, 4, 20, 2]) == 4, "Test case 2 failed"
    assert longest_consecutive([]) == 0, "Test case 3 failed"
    assert longest_consecutive([50]) == 1, "Test case 4 failed"
    assert longest_consecutive([10, 20, 30, 1, 2, 3, 4]) == 4, "Test case 5 failed"
    assert longest_consecutive([5, 6, 7, 8, 9, 1, 2, 3, 100, 101]) == 5, "Test case 6 failed"
    assert longest_consecutive([1, 2, 3, 4, 5, -1, 0]) == 7, "Test case 7 failed"
    print("All testcases passed")