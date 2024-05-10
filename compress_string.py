def compress_string(s):
    if not s:
        return ""

    output = ""
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            output += s[i] + str(count)
            count = 1

    
    output += s[-1] + str(count)
    print(output)
    return output     




assert compress_string("aabcccccaaa") == "a2b1c5a3"
assert compress_string("abcd") == "a1b1c1d1"  # "a1b1c1d1" is longer than "abcd"
assert compress_string("aaAAaa") == "a2A2a2"
assert compress_string("") == ""
assert compress_string("aaaaa") == "a5"
assert compress_string("a") == "a1"
assert compress_string("abcde") == "a1b1c1d1e1"
assert compress_string("111122223") == "142431"
assert compress_string("ababababab") == "a1b1a1b1a1b1a1b1a1b1"
assert compress_string("!!@@@####") == "!2@3#4"
assert compress_string("AaBbCc") == "A1a1B1b1C1c1"
assert compress_string("abcdefghijklmnopqrstuvwxy") == "a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1"
assert compress_string("ppppppppppppppp") == "p15"

print("All tests passed!")
