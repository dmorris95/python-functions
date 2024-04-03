#Task 1

duration = []
activity = []

def day_totals():
    check = True
    while check is True:
        if input("Would you like to add an activity for the day(y or n)?") == "y":
           activ = input("Please enter the activity you performed: ")
           activity.append(activ)
           dur = input("How long in minutes did you perform the activity? ")
           duration.append(dur)
        else:
            check = False

day_totals()
print(activity, duration)   


#Task 2

def cal_burned(activity_time):
    total = 0
    for d in activity_time:
        total += float(d)
    total = total * 3.5
    return(f"The total calories burned for the day is {total}")

cal_burned(duration)


#Task 3

def summary_func(act, time):
    c = 0 
    dur_list = []
    for t in time:
        dur_list.append(t)

    #list activities with durations
    for a in act:
        print(f"{a} was performed for {dur_list[c]} minutes")
        c += 1
    print(cal_burned(dur_list))

summary_func(activity, duration)