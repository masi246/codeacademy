def add_time(start, duration, date=None):
    weekIndex = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3,"friday":4,"saturday":5,"sunday":6}
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    days=0
    finalString = ""
    time = start.split(" ")
    curTime = time[0].split(":")
    curHour = int(curTime[0])
    curMin = int(curTime[1])
    remaining = duration.split(":")
    remainingHour = int(remaining[0])
    remainingMin = int(remaining[1])
    #Figuring out the minutes
    minutes = curMin + remainingMin
    if minutes > 60:
        curHour+=1
        minutes = abs(60-minutes)
    if minutes < 10:
        minutes = "0" + str(minutes)
    remainingHour = curHour+remainingHour
    while True:
        #Case 1: new time is before 12
        if remainingHour <=12:
            if remainingHour == 12:
                if time[1]=="PM": 
                    time[1]="AM"
                    days+=1
                else: time[1]="PM"
            finalString = str(remainingHour)+ ":" + str(minutes) + " " + str(time[1])
            if (date!=None):
                date = date.lower()
                index = int(weekIndex[date] + days)%7
                newDate = weekDays[index]
                finalString = finalString + ", "+newDate
            if days==1:
                finalString = finalString+ " (next day)"
            if days>1:
                finalString = finalString+ " (" + str(days) + " days later)"
            break
        #Case 2: new time is past 12
        else: 
            remainingHour = abs(12-(remainingHour))
            if time[1]=="PM": 
                time[1]="AM"
                days+=1
            else: time[1]="PM"
    return print(finalString)
            
