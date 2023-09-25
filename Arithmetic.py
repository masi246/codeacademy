def arithmetic_arranger(s,bool=False):
    firstLine = " "
    secondLine = ""
    thirdLine = ""
    fourthLine=" "
    for i in range(len(s)):
        nums = s[i].split()
        if(nums[1] != "+" and nums[1]!="-"):
            return(print("Error: Operator must be '+' or '-'.")) 
        if(nums[1] == "+"):
            calculation = int(nums[0]) + int(nums[2])
        else:
            calculation = int(nums[0]) - int(nums[2])
        # find the maximum length and add white spaces accordingly
        spaces = max(len(i) for i in nums) #finds the maximum length
        first = str(nums[0]).rjust(spaces," ")
        second = str(nums[2]).rjust(spaces," ")
        third=str(calculation).rjust(spaces," ")
        # create a list for the three lines
        firstLine += first + "    "
        secondLine += nums[1] + second + "   "
        thirdLine += "----   "
        fourthLine += third + "    "
    if(bool==False):
        return(print(firstLine + "\n" + secondLine + "\n"+thirdLine))
    else:
        return(print(firstLine + "\n" + secondLine + "\n"+thirdLine + "\n"+fourthLine ))
 
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)




def add_time(start, duration):
    night = False
    days = 0
    time = start.split(" ")
    curTime = time[0].split(":")
    curHour = int(curTime[0])
    curMin = int(curTime[1])
    remaining = duration.split(":")
    remainingHour = int(remaining[0])
    remainingMin = int(remaining[1])
    if time[1]=="PM":
        night=True
    minutes = curMin + remainingMin
    if minutes > 60:
        curHour+=1
        minutes = abs(60-minutes)
    if minutes < 10:
        minutes = "0" + str(minutes)
    while remainingHour > 0:
        toTwelve = 12- curHour
        curHour = 0
        remainingHour = abs(remainingHour - toTwelve)
        if toTwelve==0:
            days+=1
            night=False if night else True   
        if night:
            days+=1
            night =False
        else:
            night = True
        if remainingHour <=12 :
            curHour = remainingHour
            remainingHour = 0
    if night: 
        print(str(curHour) + ":" + str(minutes) + " PM (" + str(days) + " days later)") 
    else:
        print(str(curHour) + ":" + str(minutes) + " AM (" + str(days) + " days later)") 


add_time("3:00 PM", "3:10")



    
