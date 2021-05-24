N = map(int, input())
x, y = 1, 1
plans = input().split()

for plan in plans:

    if plan == 'L':
        y -= 1
    elif plan == 'R':
        if y == N:
            continue
        else:
            y += 1
    elif plan == 'U':
        x -= 1
    elif plan == 'D':
        if x == N:
            continue
        else:
            x += 1

    if x <= 0:
        x = 1
    elif y <= 0:
        y = 1

print(x, y)



