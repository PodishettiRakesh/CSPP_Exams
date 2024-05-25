def can_partition(nums):
    if len(nums)==2:
        if nums[0]==nums[1]:
            return True
    for i in range(len(nums)):
        nums.sort()
        lst2=nums[0:i]
        # print(lst2)
        if sum(lst2)==sum(nums[i:]):
            # print("set2 ",nums[i:])
            return True
        
    totalsum=sum(nums)
    if totalsum%2!=0:
        return False
    return False

    

    
    

# Extensive testing of the function
if __name__ == "__main__":
    # These tests will initially fail because the function does not yet have an implementation.
    assert can_partition([1, 5, 11, 5]) == True, "Test case 1 failed"
    assert can_partition([1, 2, 3, 5]) == False, "Test case 2 failed"
    assert can_partition([1, 1]) == True, "Test case 3 failed"
    # assert can_partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True, "Test case 4 failed"
    assert can_partition([20, 20]) == True, "Test case 5 failed"
    assert can_partition([2, 3, 5, 6]) == True, "Test case 6 failed"
    assert can_partition([3, 3, 3, 3, 4, 4]) == True, "Test case 7 failed"
    assert can_partition([2, 3, 3, 5, 10]) == False, "Test case 8 failed"
    assert can_partition([30, 10, 10, 10, 10]) == False, "Test case 9 failed"
    print("All testcases passed")
