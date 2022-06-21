import pandas as pd 
import numpy as np
import missingno as ms

df = pd.read_csv("./housing.csv")
print(df.head(5))
print(df.columns)

df["houseValueMinMax"] = (df.median_house_value.median() - df.median_house_value.median().min())/(df.median_house_value.median().max() - df.median_house_value.max())
print(df.head())