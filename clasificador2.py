import csv
from itertools import accumulate
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import preprocessing

labelEncoder = preprocessing.LabelEncoder()
df = pd.read_csv('AllCases1.csv')

df['score_tag'] = labelEncoder.fit_transform(df['score_tag'])
df['agreement'] = labelEncoder.fit_transform(df['agreement'])
df['subjectivity'] = labelEncoder.fit_transform(df['subjectivity'])
df['irony'] = labelEncoder.fit_transform(df['irony'])

# x = df.drop(['Class', 'score_tag', 'agreement', 'subjectivity', 'irony'], axis=1)
# x = df.drop(['Class', 'ID'], axis=1)
x = df.drop(['Class'], axis=1)
y = df['Class']
print("\nAnalisis de sentimientos")
print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)*100

matrizC = confusion_matrix(y_test, y_pred)
print(accuracy)
print(matrizC)


df = pd.read_csv('vectores1.csv')
# x = df.drop(['Class', 'ID'], axis=1)
x = df.drop(['Class'], axis=1)
y = df['Class']
print("\nVectores 1")
print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)*100

matrizC = confusion_matrix(y_test, y_pred)
print(accuracy)
print(matrizC)

# Y = Labels
# X = Features