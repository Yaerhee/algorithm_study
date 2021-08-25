import sys

word = sys.stdin.readline().rstrip().upper()
freq = dict()

for alphabet in word:
    if alphabet in freq:
        freq[alphabet] += 1
    else:
        freq[alphabet] = 1

freqCount = 0
freqChar = ''

for key, value in freq.items():
    if freqCount < value:
        freqCount = value
        freqChar = key
    elif freqCount == value:
        freqCount = value
        freqChar = '?'

print(freqChar)
