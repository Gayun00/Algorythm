import math

def calculate_distance(start, end):
    x1, y1 = start
    x2, y2 = end
    
    return abs(x2 - x1) + abs(y2 - y1)

def solution(numbers, hand):
    left_keys = [1,4,7]
    right_keys = [3,6,9]
    left = 10
    right = 11
    answer = ''
    
    keypad = {
        1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2),
        10: (3,0),
        0: (3,1),
        11: (3,2)
    }
    
    for num in numbers:
        if num in left_keys:
            left = num
            answer += "L"
        elif num in right_keys:
            right = num
            answer += "R"
        else:
            keypad_row, keypad_col = keypad[num]
            left_distance = calculate_distance(keypad[left],keypad[num])
            right_distance = calculate_distance(keypad[right],keypad[num])
            if left_distance < right_distance:
                left = num
                answer += "L"
            elif left_distance > right_distance:
                right = num
                answer += "R"
            else:
                if hand == "right":
                    right = num
                    answer += "R"
                else:
                    left = num
                    answer += "L"
    return answer