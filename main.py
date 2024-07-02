import pandas as pd
import random

# Генерация исходных данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot encoding
one_hot_data = pd.DataFrame()
one_hot_data['robot'] = [1 if x == 'robot' else 0 for x in data['whoAmI']]
one_hot_data['human'] = [1 if x == 'human' else 0 for x in data['whoAmI']]

# Вывод первых 5 строк
print(one_hot_data.head())
