import re

def solution(new_id):
    step1 = new_id.lower()
    step2 = re.sub(r'[^a-z0-9\-_.]', '', step1)
    step3 = re.sub(r'\.{2,}', '.', step2) 
    step4 = re.sub(r'^\.|\.$', '', step3) 
    
    if step4 == "":
        step4 = "a"

    if len(step4) >= 16:
        step4 = step4[:15]
        if step4[-1] == '.':
            step4 = step4[:-1]

    while len(step4) < 3:
        step4 += step4[-1]
        
    return step4
