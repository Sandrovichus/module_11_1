import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# pandas
table = pd.read_csv('employee.csv', sep=';')

print(table.head())
print('Итоговая сумма по столбцу Sum:', table['Sum'].sum())
print('Количество людей:', table['Name'].count())
print()

# matplotlib
x = ['Ivanov Petr', 'Petrov Ivan', 'Sidorov Semen']
y = [100000, 200000, 150000]
plt.bar(x, y, label='Sum')
plt.xlabel('Name')
plt.ylabel('Sum')
plt.title('Зарплаты сотрудников')
plt.show()

# numpy
array = np.array([[100, 250, 369],
                  [457, 5000, 7866],
                  [4564, 658, 0]])
print(f'Минимальное значение массива: {array.min()}')
print(f'Максимальное значение массива: {array.max()}')
print(f'Сумма всех элементов массива: {array.sum()}')
