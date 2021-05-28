N = int(input())
# 2 7 8 19 20 37 각 줄의 첫째 숫자 6 * n 차이 등차 마지막 숫자 6
if N == 1:
    print(1)
else :
    i = 1
    a = 2
    b = 7
    while True:
        if a <= N <= b:
            print(i+1)
            break
        a += i * 6
        b += (i+1) * 6
        i += 1
        