def flatten(data):
    return_list = []
    for item in data:
        if type(item) is list:
            return_list += flatten(item)
        else:
            return_list.append(item)
    return return_list

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:",example)
print("변환:",flatten(example))