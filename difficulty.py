import pandas as pd
from sklearn import preprocessing
import numpy as np
dif = pd.read_excel('sum.xlsx',header=None)
x = np.array(dif)
max_abs_scaler = preprocessing.MaxAbsScaler()
x_train_maxsbs = max_abs_scaler.fit_transform(x)
pd_x = pd.DataFrame(x_train_maxsbs)
pd_x.to_csv(difficulty)