import pandas as pd

user = pd.read_csv('dataset/user.csv', encoding='utf-8')
print(user.info())
print(user.head())
print(user['user_name'].nunique())
print(user['gender'].value_counts())

store = pd.read_csv('dataset/store.csv', encoding='utf-8')
print(store.info())
print(store.head())
print(store['store_type'].unique())
store_type = store['store_type'].unique()

for type in store_type:
    print(store[store['store_type']==type].sort_values(by='store_name'))
