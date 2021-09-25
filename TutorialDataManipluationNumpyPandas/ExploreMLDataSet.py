import numpy as np
import pandas as pd

# load the data
train = pd.read_csv("C:/Users/Michael/Python Projects/BackToPython/TutorialDataManipluationNumpyPandas/datafiles/train.csv")
test = pd.read_csv("C:/Users/Michael/Python Projects/BackToPython/TutorialDataManipluationNumpyPandas/datafiles/test.csv")

# check daata set 
train.info()

print("\nThe train data has\n", train.shape)
print("\nThe test data has\n", test.shape)

print("\nLet have a glimpse of the data set")
print(train.head())

# Checking for missing values
nans = train.shape[0] - train.dropna().shape[0]
print("\n %d rows have missing values in the train data" %nans)

nand = test.shape[0] - test.dropna().shape[0]
print("\n %d rows have missing values in the test data" %nand)

print("\nWe should be more curious to know which columns have missing values.\n")
print(train.isnull().sum())
print("\nOnly 3 columns have missing values!\n")

print("\nLet's count the number of unique values from character variables.\n")
cat = train.select_dtypes(include=['O'])
print(cat.apply(pd.Series.nunique))

print("\nSince missing values are found in all 3 character variables, let's impute these missing values with their respective modes.\n")
# Education
train.workclass.value_counts(sort= True)
train.workclass.fillna('Private', inplace= True)
# Occupation
train.occupation.value_counts(sort= True)
train.occupation.fillna('Prof-specialty', inplace= True)

# Native Country
train['native.country'].value_counts(sort= True)
train['native.country'].fillna('United-States', inplace= True)

print("\nLet's check again if there are any missing values left.\n")
print(train.isnull().sum())

print("\nNow, we'll check the target variable to investigate if this data is imbalanced or not.\nCheck the Proportion of the target variable")
print(train.target.value_counts() / train.shape[0])

print("\nWe see that 75% of the data set belongs to <=50K class. This means that even if we take a rough guess of target prediction as <=50K, we'll get 75% accuracy.") 
print("\nLet's create a cross tab of the target variable with education. With this, we'll try to understand the influence of education on the target variable.\n")

print(pd.crosstab(train.education, train.target, margins= True) / train.shape[0])

print("\nWe see that out of 75% people with <=50K salary, 27% people are high school graduates, which is correct as people with lower levels of education are expected to earn less.")
print("\nOn the other hand, out of 25% people with >=50K salary, 6% are bachelors and 5% are high-school grads. Now, this pattern seems to be a matter of concern. \nThat's why we'll have to consider more variables before coming to a conclusion.")

print("\nWe'll use the scikit learn library. Scikit learn accepts data in numeric format. Now, we'll have to convert the character variable into numeric. \nWe'll use the labelencoder function.  i.e., let's say a variable color has four values ['red','green','blue','pink'].\nLabel encoding this variable will return output as: red = 2 green = 0 blue = 1 pink = 3")

print("\nLoad sklearn and encode all object type variables\n")
from sklearn import preprocessing

for x in train.columns:
    if train[x].dtype == 'object':
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(train[x].values))
        train[x] = lbl.transform(list(train[x].values))

print(train.head())
print("\nAs we can see, all the variables have been converted to numeric, including the target variable.\n")

print("\n<50K = 0 and >50K = 1")
print(train.target.value_counts())

print("\nLets create a random forest model and check the models accuracy!\n")
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

y = train['target']
del train['target']

X = train
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1,stratify=y)

print("\nTrain the RF classifier")
clf = RandomForestClassifier(n_estimators = 500, max_depth = 6)
clf.fit(X_train,y_train)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=6, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0000001, min_samples_leaf=1,
                min_samples_split=2, min_weight_fraction_leaf=0.0,
                n_estimators=500, n_jobs=1, oob_score=False, random_state=None,
                verbose=0, warm_start=False)

clf.predict(X_test)

print("Make prediction and check model's accuracy")
prediction = clf.predict(X_test)
acc =  accuracy_score(np.array(y_test),prediction)
print ('The accuracy of Random Forest is {}'.format(acc))

print("\nLearning algorithm gave 85% accuracy.")