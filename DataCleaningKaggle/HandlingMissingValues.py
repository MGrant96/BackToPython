import pandas as pd
import numpy as np

nfl_data = pd.read_csv("./data/NFL Play by Play 2009-2018 (v5).csv", low_memory=False)

np.random.seed(0)

print(nfl_data.head())