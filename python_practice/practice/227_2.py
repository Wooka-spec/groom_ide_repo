def mul(*values):
    values_sum = 1
    for value in values:
        values_sum *= value
    return values_sum

print(mul(5, 7, 9, 10))