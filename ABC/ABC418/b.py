s = str(input())

answer = 0
for i in range(len(s)-1):
    for j in range(i+3, len(s)+1):
        tmp = s[i:j]
        if (not tmp.startswith("t")) or (not tmp.endswith("t")):
            continue
        percent = (tmp.count("t") - 2) / (len(tmp) - 2)
        answer = max(answer, percent)

print(answer)