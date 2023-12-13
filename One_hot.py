# Решение с get_dummies.
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data = pd.get_dummies(data, columns=['whoAmI']).astype(int)
data.head()
print(data)

# Решение без использования get_dummies.

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
categories = data['whoAmI'].unique()

for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)

data.drop('whoAmI', axis=1, inplace=True)
data.head()
print(data)
