from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    users = defaultdict(set)  # 중복을 제거하기 위해 set 사용
    mail = defaultdict(int)

    for rep in report:
        user, target = rep.split()
        if target not in users[user]:
            users[user].add(target)
            mail[target] += 1

    for user in id_list:
        count = sum(1 for target in users[user] if mail[target] >= k)
        answer.append(count)

    return answer