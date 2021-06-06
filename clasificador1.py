import csv
from itertools import accumulate
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

training = [] # Guarda diccionario entrada en una lista
testing = []
labelEncoder = preprocessing.LabelEncoder()
df = pd.read_csv('AllCases1.csv')

df['score_tag'] = labelEncoder.fit_transform(df['score_tag'])
df['agreement'] = labelEncoder.fit_transform(df['agreement'])
df['subjectivity'] = labelEncoder.fit_transform(df['subjectivity'])
df['irony'] = labelEncoder.fit_transform(df['irony'])

# x = df.drop(['Class', 'score_tag', 'agreement', 'subjectivity', 'irony'], axis=1)
# x = df.drop(['Class', 'ID'], axis=1)
x = df.drop(['Class'], axis=1)

print(x)
y = df['Class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

gnb = GaussianNB()
gnb.fit(x_train, y_train)

y_pred = gnb.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)*100
print(accuracy)
# y_pred = gnb.fit(X_train, y_train).predict(X_test)
# print("Number of mislabeled points out of a total %d points : %d"

# Y = Clase
# X = Atributos

# Y = Labels
# X = Features
# % (X_test.shape[0], (y_test != y_pred).sum()))