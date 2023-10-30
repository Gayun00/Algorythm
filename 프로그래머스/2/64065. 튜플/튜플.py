import re

def solution(s):
    pattern = r'\},\{'
    tuple_strings = re.split(pattern, s[1:len(s)-1])
    dict = {}

    for tuple_string in tuple_strings:
        trimmed = tuple_string.replace('{', '').replace('}', '')
        splited = re.split(',',trimmed)
        for el in splited:
            if int(el) not in dict:
                dict[int(el)] = 0
            else:
                dict[int(el)] += 1
                
    print(dict,list(dict))
    
    return sorted(dict, key=lambda x: dict[x], reverse=True)
