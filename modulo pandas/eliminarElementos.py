import pandas as pd
import numpy as np

np.arange(4)
serie = pd.Series(np.arange(4), index=['a','b','c','d'])
print(serie)  # a    0
              # b    1
              # c    2
              # d    3

borrar = serie.drop('c')
print(borrar)  # a    0
               # b    1
               # d    3




