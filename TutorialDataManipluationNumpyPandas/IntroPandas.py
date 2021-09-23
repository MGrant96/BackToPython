# Pandas
import pandas as pd
print("Create a data frame")
data = pd.DataFrame({'Country': ['Russia', 'Columbia', 'Chile', 'Equador', 'Nigeria'],'Rank':[121, 40, 100, 130, 11]})
print("\n", data)

# Quick analysis of any data set with 
print("\nQuick Analysis of dataset with describe()", data.describe())
data.info()

data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print("\n", data)

print("\nLet's sort the data frame by ounces - inplace = True will make changes to the data", 
data.sort_values(by = ['ounces'], ascending = True, inplace = False))

print("\nWe can sort the data by not just one column but multiple columns as well.")

print("\n", data.sort_values(by = ['group', 'ounces'], ascending = [ True, False ], inplace = False))











