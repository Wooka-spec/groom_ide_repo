N = int(input('배열의 원소 수>'))
num_list = []

for i in range(N):
    num_list.append(int(input('>')))
    
num_list = sorted(num_list)
print('정렬된 리스트>', num_list)
    
s_idx = 0
e_idx = N-1
m_idx = (s_idx + e_idx) // 2

search = int(input('검색할 값'))

while True:
    m_idx = (s_idx + e_idx) // 2
    if num_list[m_idx] == search:
        print('검색성공')
    elif num_list[m_idx] < search:
        s_idx = m_idx + 1
    else:
        e_idx = m_idx - 1
    if s_idx > m_idx:
        print('검색 실패!')
        break

    