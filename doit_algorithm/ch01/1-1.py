print('세 정수의 최대값을 입력하세요')

a = int(input('a >'))
b = int(input('b >'))
c = int(input('c >'))

maxnum = a 
if b > maxnum:
    maxnum = b
if c > maxnum:
    maxnum = c
# 7~11행은 순차적으로 실행된다 이렇게 한 문장씩 처리되는 구조를 순차구조라고 한다.
# 8~11행은 if 조건문을 사용한 복합문이며 조건식으로 평가한 결과에 따라 프로그램의 실행흐름이 변경된다.
#    이러한 구조를 선택구조 라고한다
    
print('최대 값은 %d 입니다' %maxnum)