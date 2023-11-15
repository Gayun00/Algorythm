import math
import operator


def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    dict = {}
    times = {}
    latest = (23 * 60) + 59

    for record in records:
        time, num, behavior = record.split()
        minute = int(time[:2]) * 60 + int(time[3:5])
        if num not in times:
            times[num] = 0

        if behavior == "OUT":
            diff_time = minute - dict[num]
            times[num] += diff_time
            del dict[num]
        else:
            dict[num] = minute

    for di in dict:
        diff_time = latest - dict[di]
        times[di] += diff_time

    for num in times:
        if times[num] <= default_time:
            times[num] = default_fee
        else:
            times[num] = (
                default_fee
                + math.ceil((times[num] - default_time) / unit_time) * unit_fee
            )

    return [value for key, value in sorted(times.items(), key=(operator.itemgetter(0)))]
