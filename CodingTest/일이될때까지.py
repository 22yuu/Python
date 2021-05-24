num, k = map(int, input().split())
cnt = 0


while(True):

    if num <= 1:
        break

    if num % k == 0:
        num /= k
        cnt += 1
    else:
        num -= 1
        cnt += 1
    print(num)
print(cnt)


