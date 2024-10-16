s1,s2,s3 = map(str, input().split())

if s1 == "<":
    if s2 == "<":
        if s3 == "<":
            print("B")
        else:
            print("C")
    else:
        if s3 == "<":
            print("C")
        else:
            print("A")
else:
    if s2 == "<":
        if s3 == "<":
            print("A")
        else:
            print("B")
    else:
        if s3 == "<":
            print("C")
        else:
            print("B")