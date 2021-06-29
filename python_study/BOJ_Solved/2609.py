def euclidean(a, b):
    r = b % a
    if r == 0:
        return a
    else:
        return  euclidean(r, a)
    

A, B = map(int, input().split())

gcd = euclidean(A, B)
print(gcd)
print(gcd * (A // gcd) * (B // gcd))
