import sys

word = sys.stdin.readline().rstrip()
freq = dict()

for alphabet in word:
    if alphabet in freq:
        freq[alphabet] += 1
    else:
        freq[alphabet] = 1

print(freq)
word = list(freq.keys())
f = list(freq.values())



print(word)
print(f)

print(alphabet.find(max(freq.keys())))