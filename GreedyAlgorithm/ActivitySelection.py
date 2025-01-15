def activity_selection(activities):
    activities.sort(key=lambda x:x[1])
    selects=[]
    last_end_time=0
    for start , end in activities:
        if start >= last_end_time:
            selects.append((start,end))
            last_end_time=end
    return selects
#测试
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
print(activity_selection(activities))  # [(1, 4), (5, 7), (8, 11), (12, 14)]