import string

def generate(alphabet, max_len):
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len-1):
            yield c + next


options = list(generate('abc', 3))
for val in generate('abc', 3):
    print(val)

print(options)


"""
    If comparing to hashes, you will need to encode all password options before 
    passing such generated sttings to a hashing function.
    string.ascii_letters.encode('uft-8')
"""