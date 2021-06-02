character= {
    "name" : "wooka",
    "level" : 51,
    "items" : {
        "sword" : "blade",
        "armor" : "steel"
    },
    "skill" : ["swing","smite","swwwwwwing"]
}

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]: #character[key]를 쓰는 이유는 key 라고 쓸경우 key 가 리스트나 딕셔너리 형태가아닌 문자열 형태로 받아지기 때문
            print(small_key,":",character[key][small_key])
    
    elif type(character[key]) is list:
        for item in character[key]:
            print(key,":",item)
            
    else:
        print(key,":",character[key])