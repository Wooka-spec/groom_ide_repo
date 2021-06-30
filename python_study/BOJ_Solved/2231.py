N = int(input())

mom_num = N - (9 * len(str(N)))
if mom_num < 0:
    mom_num = 0

while mom_num <= N:
    mom_num_result = mom_num
    str_mom_num = str(mom_num)
    for i in range(len(str_mom_num)):
        mom_num_result += int(float(str_mom_num[i]))
    if mom_num_result == N:
        print(mom_num)
        break
    mom_num += 1

if mom_num -1 == N:
    print(0)
    
    