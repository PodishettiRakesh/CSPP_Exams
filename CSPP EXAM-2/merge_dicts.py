def merge_dicts(d1, d2):
    for key,value in d2.items():
        if key in d1:
            d1[key]=value
        else:
            d1[key]=value
    print(d1)
    return d1

# Extensive testing of the function
if __name__ == "__main__":
    # These tests should fail initially as the function does not yet have an implementation.
    assert merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 3, 'c': 4}, "Test case 1 failed"
    assert merge_dicts({}, {'a': 10, 'b': 20}) == {'a': 10, 'b': 20}, "Test case 2 failed"
    assert merge_dicts({'x': 5}, {}) == {'x': 5}, "Test case 3 failed"
    assert merge_dicts({'k': 7}, {'k': 8, 'j': 9}) == {'k': 8, 'j': 9}, "Test case 4 failed"
    assert merge_dicts({'m': 33}, {'n': 44}) == {'m': 33, 'n': 44}, "Test case 5 failed"
    assert merge_dicts({'alpha': 100, 'beta': 200}, {'beta': 300, 'gamma': 400}) == {'alpha': 100, 'beta': 300, 'gamma': 400}, "Test case 6 failed"
    print("All testcases passed")