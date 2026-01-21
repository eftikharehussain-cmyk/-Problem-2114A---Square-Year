# -Problem-2114A---Square-Year
for _ in range(int(input())):
    s = input()
    s1 = int(s)

    _sqrt = -1
    for i in range(0, 100):
        if i * i == s1:
            _sqrt = i
            break
    if _sqrt == -1:
        print(-1)
    else:
        print(0, _sqrt)

