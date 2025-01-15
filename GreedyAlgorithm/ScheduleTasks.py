class Task:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return f"({self.start}, {self.end}, {self.weight})"


def schedule_tasks(tasks):
    # 1. 按任务的结束时间排序
    tasks.sort(key=lambda x: x.end)

    # 2. 贪心选择不冲突的任务
    selected_tasks = []
    last_end_time = 0  # 记录上一个任务的结束时间
    total_weight = 0  # 记录任务总权重

    for task in tasks:
        if task.start >= last_end_time:  # 选择不冲突的任务
            selected_tasks.append(task)
            total_weight += task.weight
            last_end_time = task.end  # 更新结束时间

    return selected_tasks, total_weight


# 示例任务（开始时间, 结束时间, 权重）
tasks = [Task(1, 4, 5), Task(2, 6, 6), Task(5, 8, 8), Task(7, 9, 7), Task(8, 10, 6)]

# 调度任务
selected_tasks, total_weight = schedule_tasks(tasks)
print("Selected tasks:", selected_tasks)
print("Total weight:", total_weight)
