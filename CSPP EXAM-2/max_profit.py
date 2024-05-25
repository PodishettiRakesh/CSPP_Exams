def max_profit(prices):
    profit=0
    for i in range(len(prices)-1):
        # print(prices[i])
        # print("--------")
        for j in range(i+1,len(prices)):
            # print(prices[j])
            # print("===============")
            
            if prices[j]-prices[i]>profit:
                profit=prices[j]-prices[i]
                # print("profit:",profit)
    print(profit)
    return profit
        


# Extensive testing of the function
if __name__ == "__main__":
    # These tests will initially fail because the function does not yet have an implementation.
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Test case 1 failed"
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test case 2 failed"
    assert max_profit([1, 2, 3, 4, 5]) == 4, "Test case 3 failed"
    assert max_profit([1, 6, 2, 8, 3, 10]) == 9, "Test case 4 failed"
    assert max_profit([10, 20, 30, 40, 50]) == 40, "Test case 5 failed"
    assert max_profit([100, 90, 80, 70, 60]) == 0, "Test case 6 failed"
    assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 4, "Test case 7 failed"
    assert max_profit([14, 9, 10, 12, 4, 8, 1, 16]) == 15, "Test case 8 failed"
    print("All testcases passed")
