import sys

word = sys.stdin.readline()
count = 0

for i in range(len(word)):
    if word[i] == 'c' or word[i] == 's' or word[i] == 'z':
        if word[i+1] == '=':
            count += 1
    elif word[i] == 'c' or word[i] == 'd':
        if word[i+1] == '-':
            count += 1
    elif word[i] == 'l' or word[i] == 'n' and word[i+1] == 'j':
        count += 1
    elif word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=':
        count += 1
    # else:
    #     count += 1

print(count)


