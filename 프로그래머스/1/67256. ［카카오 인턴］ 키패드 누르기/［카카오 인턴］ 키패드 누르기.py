def checkDistance(start, end):
    x1, y1 = start
    x2, y2 = end
    
    return abs(x2 - x1) + abs(y2 - y1)

def solution(numbers, hand):
    result = ""
    left_keys = [1,4,7]
    right_keys = [3,6,9]
    cur_left = "*"
    cur_right="#"
    
    keypad = {
        1:(0,0),
        2:(0,1),
        3:(0,2),
        4:(1,0),
        5:(1,1),
        6:(1,2),
        7:(2,0),
        8:(2,1),
        9:(2,2),
        "*":(3,0),
        0:(3,1),
        "#":(3,2)
    }
    
    for number in numbers:
        if number in left_keys:
            cur_left = number
            result += "L"
            continue
        elif number in right_keys:
            cur_right = number
            result += "R"
            continue
            
        if checkDistance(keypad[cur_left],keypad[number]) > checkDistance(keypad[cur_right],keypad[number]):
            cur_right = number
            result += "R"
        elif checkDistance(keypad[cur_left],keypad[number]) == checkDistance(keypad[cur_right],keypad[number]):
            if hand == "right":
                cur_right = number
                result += "R"
            else:
                cur_left = number
                result += "L"
        else:
            cur_left = number
            result += "L"
            
    return result
            

 