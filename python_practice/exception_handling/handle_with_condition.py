user_input_a = input("정수입력 > ")

if user_input_a.isdigit(): #입력받은 값이 숫자로만 구성되어 있는가
    number_input_a = int(user_input_a)
    print("원의 반지름 :",number_input_a)
    print("원의 둘레 :", 2 * 3.14 * number_input_a)
    print("원의 넓이 :",3.14 * number_input_a ** 2)
    
else:
    print("정수를 입력해 주세요!")
    