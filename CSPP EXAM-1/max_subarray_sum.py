import itertools
def max_subarray_sum(nums):

    if len(nums) == 1:
        return nums[0]  
    max_sum = float('-inf')  
    current_sum = 0 
    for num in nums:
        current_sum = max(num, current_sum + num)  
        max_sum = max(max_sum, current_sum) 
    print(max_sum) 
    return max_sum
    
    


# assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_sum([1]) == 1
assert max_subarray_sum([-1, -2, -3]) == -1
assert max_subarray_sum([2, 3, 4, 5]) == 14
assert max_subarray_sum([-4, -2, -8, -1]) == -1
assert max_subarray_sum([0, -1, 0, -2, 0]) == 0
assert max_subarray_sum([0, 1, 2, -1, 2, 3, -5, 4]) == 7
assert max_subarray_sum([0]) == 0
assert max_subarray_sum([100, -90, 100, -80, 100]) == 130 

print("All tests passed!")
