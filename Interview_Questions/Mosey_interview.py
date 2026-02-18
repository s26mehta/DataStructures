# Task: Implement a function that matches a string against a pattern.
# A pattern is defined as a list of operators, each of which is a list
# containing the name of the operator and its arguments. There are
# only three operators.
#
# Here is an example pattern:
#
#    [
#        ["req", "a"],      # "a" is required
#        ["alt", "b", "c"], # either "b" or "c" is required
#        ["opt", "d"],      # "d" is optional
#    ]
#
# The only strings that match are: "ab", "ac", "abd", and "acd".
#
# Your match function must accept a pattern and a string. It must
# return True if the string completely matches the pattern, otherwise
# it returns False.
"""
["req", "a"],
["req", "b"]
["alt", "c", "d"]
["req", "e"]
["opt", "f"]
"""

# from enum import Enum

# class OptName(Enum):
#     REQ: "req"
#     ALT: "alt"
#     OPT: "opt"

["a", ("b", ""), ("b", "c"), "d"]
option_tracker = []
output = "abd"

def match(pattern, text):
    if len(pattern) == 0 and len(text) != 0:
        return False

    opt_chars = []
    for opt in pattern:
        if opt[0] == "req":
            opt_chars.append([opt[1]])
        elif opt[0] == "alt":
            opt_chars.append(sorted([opt[1], opt[2]]))
        elif opt[0] == "opt":
            opt_chars.append(["", opt[1]])
        else:
            print("Unknown operator")

    if len(text) > len(opt_chars):
        return False

    # print(opt_chars)
    opt_idx = 0
    text_idx = 0
    while True:
        if text_idx == len(text) - 1 and opt_idx == len(
                opt_chars) - 1 and text[text_idx] in opt_chars[opt_idx]:
            return True
        if text_idx == len(text) - 1 and text[text_idx] not in opt_chars[
                opt_idx] and "" not in opt_chars[opt_idx]:
            return False

        # print("llll", text, text_idx, opt_chars, opt_idx)
        if text[text_idx] not in opt_chars[opt_idx]:
            # print('here1')
            return False

        if "" in opt_chars[opt_idx] and text[text_idx] not in opt_chars[
                opt_idx]:
            # print('here2')
            if opt_idx < len(opt_chars):
                opt_idx += 1
                continue
            else:
                return False

        if text_idx < len(text) - 1:
            text_idx += 1
        if opt_idx < len(opt_chars) - 1:
            opt_idx += 1
    # print('heresss')
    return True


TEST_1 = {
    "pattern": [
        ["req", "a"],
        ["req", "b"],
    ],
    "test_cases": [
        ["ab", True],
        ["abc", False],
        ["ba", False],
        ["a", False],
        ["b", False],
    ],
}

TEST_2 = {
    "pattern": [
        ["req", "a"],
        ["opt", "b"],
        ["req", "c"],
    ],  # => (ac, abc)
    "test_cases": [
        ["abc", True],
        ["ab", False],
        ["ac", True],
        ["ca", False],
        ["cba", False],
        ["a", False],
        ["abcd", False],
    ],
}



TEST_3 = {
    "pattern": [
        ["req", "a"],
        ["opt", "b"]
        ["alt", "b", "c"],
        ["req", "d"],
    ],
    "test_cases": [
        ["abd", True],
        ["acd", True],
        ["abcd", False],
        ["ab", False],
        ["ac", False],
        ["ad", False],
        ["bd", False],
        ["bc", False],
    ],
}

TEST_4 = {
    "pattern": [
        ["opt", "a"],
        ["req", "b"],
        ["alt", "c", "d"],
    ],
    "test_cases": [
        ["abc", True],
        ["abd", True],
        ["ab", False],
        ["ac", False],
        ["ad", False],
        ["ba", False],
        ["bc", True],
        ["bd", True],
        ["bcd", False],
        ["d", False],
        ["abcd", False],
    ],
}

TEST_5 = {
    "pattern": [
        ["req", "a"],
        ["req", "b"],
        ["opt", "c"],
    ],
    "test_cases": [
        ["abc", True],
        ["abd", False],
        ["ab", True],
        ["ac", False],
        ["ad", False],
        ["ba", False],
        ["bc", False],
        ["abcd", False],
    ],
}


def run_tests():
    for test in [TEST_1, TEST_2, TEST_3, TEST_4, TEST_5]:
        pattern = test["pattern"]
        print(f"TESTING: {pattern}")
        for text, should_match in test["test_cases"]:
            if match(pattern, text) == should_match:
                message = "matches" if should_match else "does not match"
                print(f"PASS '{text}' {message}")
            else:
                message = "should match" if should_match else "should not match"
                print(f"FAIL '{text}' {message}")
        print("")


print(run_tests())