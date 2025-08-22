def reversestring(words):
    lst=words.strip().split()
    lst.reverse()
    return ' '.join(lst)


#  Test cases
inputs = [
    "the sky is blue",
    "  hello world  ",
    "a good   example",
    "    ",
    "word"
]

for inp in inputs:
    print(f'Input: "{inp}"')
    print(f'Output: "{reversestring(inp)}"\n')