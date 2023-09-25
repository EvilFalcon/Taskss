import pulp
import matplotlib.pyplot as plt

# Исходные данные для задачи 1
a1 = 19
a2 = 16
a3 = 19
b1 = 26
b2 = 17
b3 = 8
c1 = 868
c2 = 638
c3 = 853
alpha = 5
beta = 4

# Создание оптимизационной задачи
prob = pulp.LpProblem("MaximizeProfit", pulp.LpMaximize)

# Определение переменных решения
x = pulp.LpVariable("xA", lowBound=0)
y = pulp.LpVariable("xB", lowBound=0)

# Определение целевой функции
prob += alpha * x + beta * y

# Добавление ограничений на использование материалов
prob += a1 * x + b1 * y <= c1
prob += a2 * x + b2 * y <= c2
prob += a3 * x + b3 * y <= c3

# Решение задачи линейного программирования
prob.solve()

# Вывод результатов
print("Максимальная прибыль:", pulp.value(prob.objective))
print("Количество продукции A:", pulp.value(x))
print("Количество продукции B:", pulp.value(y))

# Построение векторного графика
fig, ax = plt.subplots()
ax.quiver(0, 0, pulp.value(x), pulp.value(y), angles='xy', scale_units='xy', scale=1, color='blue')
ax.set_xlim([0, max(pulp.value(x),pulp.value(y)) + 10])
ax.set_ylim([0, max(pulp.value(x),pulp.value(y)) + 10])
plt.xlabel("Product A")
plt.ylabel("Product B")
plt.title("Optimal Production")
plt.grid()
plt.show()