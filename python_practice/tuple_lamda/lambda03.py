list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x:x * x,list_input_a)
print("#map 함수의 실행결과")
print("map(lambda x: x * x,list_input_a):",output_a)
print("map(lambda x: x * x,list_input_a:",list(output_a))
print()

output_b = filter(lambda x : x < 3, list_input_a)
print("#filter 함수의 실행결과")
print("filter(lambda x: x < 3, list_input_a):",output_b)
print("filter(lambda x: x < 3, list_input_a):",list(output_b))
print()