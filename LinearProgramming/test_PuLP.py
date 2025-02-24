import pulp

# 创建一个线性规划问题，目标是最大化
prob = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# 定义决策变量，x1 和 x2 都是非负的
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

# 定义目标函数
prob += x1 + 2 * x2, "Objective Function"

# 添加约束
prob += x1 + x2 <= 5
prob += 2 * x1 + x2 <= 6

# 求解线性规划问题
prob.solve()

# 输出结果
print(f"Optimal value of x1: {x1.varValue}")
print(f"Optimal value of x2: {x2.varValue}")
print(f"Maximum value of the objective function: {pulp.value(prob.objective)}")
