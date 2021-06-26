A, B = map(int, input().split())

if A > B:
    big_num = A
    small_num = B
else:
    big_num = B
    small_num = A

r_bignum = big_num
r_smallnum = small_num

r = 12345
while r == 0:
    r = big_num % small_num
    big_num = small_num
    big_num = r
    
print(big_num)
print(big_num * r_bignum * r_smallnum)