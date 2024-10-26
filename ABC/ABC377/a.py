s = input()
#並び変えて、"ABC"と一致するかを全探索
s1 = "".join(sorted(s))

if s1 == "ABC":
    print("Yes")
else:
    print("No")