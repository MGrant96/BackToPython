# Pandas 
# nodemon --exec python intropandas.py

import pandas as pd
import numpy as np
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

print("\n", data.sort_values(by = ['group', 'ounces'], ascending = [ True, False ], inplace = False), "\n")

print("Get rid of Duplicate rows in dataset!")
print("\ncreate another data with duplicated rows")
data = pd.DataFrame({'k1':['one'] * 3 + ['two'] * 4, 'k2': [3,2,1,3,3,4,4]})
print("\n", data)

print("\nSort the values!\n")
data.sort_values(by='k2')
print("\n", data)

print("\nRemove duplicates!")
print(data.drop_duplicates())
print("Here, we removed duplicates based on matching row values across all columns.")

print("Alternatively, we can also remove duplicates based on a particular column. \nLet's remove duplicate values from the k1 column.")
print(data.drop_duplicates(subset = 'k1'))

print("\nNow, we will learn to categorize rows based on a predefined criteria. It happens a lot while data processing where you need to categorize a variable. \nFor example, say we have got a column with country names and we want to create a new variable 'continent' based on these country names.")
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

print("\nNow, we want to create a new variable which indicates the type of animal which acts as the source of the food. \nTo do that, first we'll create a dictionary to map the food to the animals. Then, we'll use map function to map the dictionary's values to the keys. ")
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'


#create a new variable
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print("\n", data)

print("\nanother way of doing it is: convert the food values to the lower case and apply the function\n")
lower = lambda x: x.lower()
data['food'] = data['food'].apply(lower)
data['animal2'] = data.apply(meat_2_animal, axis='columns')
print(data)

print(data.assign(new_variable = data['ounces']*10))

print("\nLets remove animal2 column from the data frame!\n")
data.drop('animal2', axis= 'columns', inplace= True)
print(data)

print("\nWe frequently find missing values in our data set. A quick method for imputing missing values is by filling the missing value with any random number. \nNot just missing values, you may find lots of outliers in your data set, which might require replacing.")
print("\nSeries function from pandas are used to create arrays\n")
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)

print("\nreplace -999 with NaN values\n")
data.replace(-999, np.nan, inplace = True)
print(data)

print("\nWe can also replace multiple values at once.\n")
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data.replace([-999,-1000], np.nan, inplace= True)
print(data)

print("\nHow to rename column names and axis (row names)\n")
data = pd.DataFrame(np.arange(12).reshape((3, 4)), index= ['Ohio', 'Colorado', 'New York'], columns= ['one', 'two', 'three', 'four'])
print(data)

print("\nUsing rename function\n")
data.rename(index = {'Ohio':'SanF'}, columns={'one':'one_p','two':'two_p'}, inplace= True)
print(data)

print("\nYou can also use string functions\n")
data.rename(index = str.upper, columns= str.title, inplace= True)
print(data)

print("\nHow to categorize (bin) continuous variables\n")
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
print("\nWe'll divide the ages into bins such as 18-25, 26-35,36-60 and 60 and above.\n'(' means the value is included in the bin, '[' means the value is excluded")
print("\n", cats)

print("\nTo include the right bin value, we can do:")
print(pd.cut(ages,bins,right=False))

print("\npandas library intrinsically assigns an encoding to categorical variables.")
print(cats.codes)

print("\nLet's check how many observations fall under each bin")
print(pd.value_counts(cats))

# We can pass a unique name to each label
bin_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']
new_cats = pd.cut(ages, bins, labels=bin_names)
print("\n", pd.value_counts(new_cats))

print("\nWe can also calculate their cumulative sum!\n")
print(pd.value_counts(new_cats).cumsum())

"""grouping data and creating pivots in pandas."""
print("\ngrouping data and creating pivots in pandas.\n")

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})

print(df)

print("\nCalculate the mean of data1 column by key1")
grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())

print("\nlet's see how to slice the data frame\n")
dates = pd.date_range('20130101', periods= 6)
df = pd.DataFrame(np.random.randn(6, 4), index= dates, columns= list('ABCD'))
print(df)

print("\nGet the first n rows from the date frame")
print(df[:3])

print("\nSlice based on the Dates!\n")
print(df['20130101':'20130104'])

print("\nSliced based on Column names\n")
print(df.loc[:, ['A','B']])

print("\nWe can slice on row index labels and column names\n")
print(df.loc['20130102':'20130103',['A','B']])

print("\nSlice based on index of columns\n")
print(df.iloc[3]) #returns 4th row (index is 3rd)

print("\nreturns a specific range of rows")
print(df.iloc[2:4, 0:2])

print("\nBoolean indexing based on column values as well. This helps in filtering a data set based on a pre-defined condition.\n")
print(df[df.A > 1])

print("\nWe can copy the dataset")
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

print("\nselect rows based on column values\n")
print(df2[df2['E'].isin(['two','four'])])

print("\nselect all rows except those with two and four\n")
print(df2[~df2['E'].isin(['two', 'four'])])

print("\nlist all columns where A is greater than C\n")
print(df.query('A > C'))

print("\nQuery using the OR condition\n")
print(df.query('A < B | C > A'))

print("\nPivot tables are extremely useful in analyzing data using a customized tabular format. It offers a super-quick way to analyze data.\n")
# Create a data frame
data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

print("\nCalculate the means of each group")
print(data.pivot_table(values= 'ounces', index= 'group', aggfunc=np.mean))

print("\nCalculate count by each group\n")
print(data.pivot_table(values= 'ounces', index= 'group', aggfunc= 'count'))

