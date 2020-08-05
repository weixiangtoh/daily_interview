"""
A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. 
An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
"""
def next_number(s):
    result = []
    i = 0
    while i < len(s):
        # check if right is the same as left
        # if equal then must count how many times repeated
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)

# s = '1211'
# print(next_number(s))

def LookSaySeq(n):
    s = '1'
    for i in range(n-1):
        s = next_number(s)
    return s

print(LookSaySeq(4))