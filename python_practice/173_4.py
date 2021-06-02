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
        for small_key in character[key]:
            print(small_key,":",character[key][small_key])
    
    elif type(character[key]) is list:
        for item in character[key]:
            print(key,":",item)
            
    else:
        print(key,":",character[key])