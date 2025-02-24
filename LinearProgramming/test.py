import numpy as np
from scipy.optimize import linprog

# 定义目标函数系数（负号表示最大化）
c = [-1, -2]  # Maximize: x1 + 2x2
#在 scipy.optimize.linprog() 中默认是最小化目标函数。因此，为了将最大化问题转化为最小化问题，我们对目标函数系数取负，
# 即 c = [-1, -2]。这样，linprog 会最小化 -x1 - 2x2，这等价于最大化 x1 + 2x2。

# 定义约束条件
A = [[1, 1], [2, 1]]
b = [5, 6]

# 定义变量的边界
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# 求解线性规划
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

print("Optimal solution:", res.x)
print("Maximum value of the objective function:", -res.fun)
