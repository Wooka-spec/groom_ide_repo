try:
    number_input_a = int(input("정수를 입력해 주세요 >"))
    print("원의 반지름 :",number_input_a)
    print("원의 둘레 :", 2 * 3.14 * number_input_a)
    print("원의 넓이 :",3.14 * number_input_a ** 2)
except:
    print("정수를 입력하세요")
else:
    print("예외가 발생하지 않았습니다")
finally:
    print("프로그램 동작 완료")