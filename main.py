import operator
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
difficulty = pd.read_csv('difficulty.csv')
y = pd.read_csv('y.csv')
word = data.iloc[:,3]

def count_each_char_sort_value(str):
    dict = {}
    for i in str:
        dict[i] = dict.get(i, 0) + 1
    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    return dict

x = []
for i in range(0,355):
    x.append(count_each_char_sort_value(word[i]))
x_pd = pd.DataFrame(x)

first_char = []
for i in range(0,355):
    first_char.append(ord(word[i][0])-97)

repeat_char = []
for i in range(0,355):
    if(x_pd.iloc[i,4]==None):
        if(x_pd.iloc[i,3]==None):
            repeat_char.append(2)
        else:
            repeat_char.append(1)
    else:
        repeat_char.append(0)
df1 = pd.DataFrame(repeat_char, columns=['repeat'])
df1.insert(1, 'first_char', first_char,allow_duplicates = False)
df1.to_csv('x.csv')