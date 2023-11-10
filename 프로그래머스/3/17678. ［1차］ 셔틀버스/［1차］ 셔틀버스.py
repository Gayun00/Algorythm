def solution(n, t, m, timetable):
    answer = 0
    
    crewTime = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    
    busTimes = [9*60 + t*i for i in range(n)]
    
    can_ride_bus_idx = 0
    
    for busTime in busTimes:
        crew_on_bus = 0
        
        while crew_on_bus < m and can_ride_bus_idx < len(crewTime) and crewTime[can_ride_bus_idx] <= busTime:
            can_ride_bus_idx += 1
            crew_on_bus += 1
            
        if crew_on_bus < m:
            answer = busTime
        else:
            answer = crewTime[can_ride_bus_idx - 1] - 1
            
    return str(answer//60).zfill(2) + ":" + str(answer % 60).zfill(2)
    