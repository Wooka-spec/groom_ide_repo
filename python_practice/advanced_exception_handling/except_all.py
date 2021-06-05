list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소:{}".format(number_input, list_number[number_input]))
    예외.발생()
except ValueError:
    print("정수를 입력해 주세요")
except IndexError:
    print("리스트의 범위를 벗어났습니다")
except Exception as exception:
    print("예상치 못한 오류가 발생했습니다")
    print("exception:",exception)
    