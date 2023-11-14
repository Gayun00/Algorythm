from collections import defaultdict

def solution(record):
    answer = []
    record_dict = defaultdict(list)
    for text in record :

        text = text.split(" ")
        if len(text) > 2 : 
            record_dict[text[1]] = text[-1]

    for text in record : 
        text = text.split(" ")
        if text[0] == 'Enter':
            data = record_dict[text[1]]
            data+='님이 들어왔습니다.'
            answer.append(data)

        elif text[0] == 'Leave':
            data = record_dict[text[1]]
            data+='님이 나갔습니다.'
            answer.append(data)

    return answer


    return answer
