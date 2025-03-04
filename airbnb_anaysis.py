import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AB_NYC_2019/AB_NYC_2019.csv') #load dataset

#display basic info
print("Dataset info:\n")
print(df.info())
print("\nFirst five rows:\n")
print(df.head())