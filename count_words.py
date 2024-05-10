def count_words(text):
    if len(text) == 0:
        return {}
    dic = {}
    words = text.split(" ")
    for each in words:

        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1
    print(dic)
    return dic
    

assert count_words("hello world hello") == {'hello': 2, 'world': 1}
assert count_words("one two three two three three") == {'one': 1, 'two': 2, 'three': 3}
assert count_words("") == {}
assert count_words("Hello hello HeLLo") == {'Hello': 1, 'hello': 1, 'HeLLo': 1}
assert count_words("123 123 abc123 123abc") == {'123': 2, 'abc123': 1, '123abc': 1}
assert count_words("word " * 1000 + "anotherword") == {'word': 1000, 'anotherword': 1}

print("All tests passed!")
