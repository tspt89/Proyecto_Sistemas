import csv
from os import replace
import string
import math

from nltk.corpus import stopwords
from nltk.corpus.reader import lin
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.util import pr

count = dict()      # Todos

# Cuenta las palabras segun su clasificacion
def word_count(str):
    words = []
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1


# lowercase
with open('./TrainingDS.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    entrada = dict()  # Diccionario para asignar id con su respectiva palabra
    saveIn = [] # Guarda diccionario entrada en una lista

    next(csv_reader)
    lmtzr = WordNetLemmatizer()
    
    for line in csv_reader:
        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
            
        text = ''.join([i for i in line[1].translate(translator) if i not in string.punctuation]).lower().split(' ')
        

        NoStopWords = [lmtzr.lemmatize(x) for x in text if not x in stopwords.words('english')] # lema y palabras cerradas
        entrada["ID"] = int(line[0])
        entrada["Text"] = ' '.join(NoStopWords)
        entrada["Class"] = int(line[2])
        entrada["score_tag"] = line[3]
        entrada["agreement"] = line[4]
        entrada["subjectivity"] = line[5]
        entrada["confidence"] = int(line[6])
        entrada["irony"] = line[7]
        entrada["Happy"] = float(line[8])
        entrada["Fear"] = float(line[9])
        entrada["Sad"] = float(line[10])
        entrada["Bored"] = float(line[11])
        entrada["Angry"] = float(line[12])
        entrada["Excited"] = float(line[13])

        # print(entrada["Text"])
        saveIn.append(dict(entrada))
    
    # frecuencia simple
    for line in saveIn:
        word_count(line["Text"])

    # palabras mas frecuentes
    count = sorted(count.items(), key=lambda k: k[1], reverse=True)
    count = dict((x, y) for x, y in count)
    countL = len(count)
    
    # frecuencia inversa del documento
    idf = []
    idf = dict((line,math.log(countL/count[line])) for line in count)
    
    tf = []
    
    # Vectores
    # Puede optimizarse
    for line in saveIn:
        for x in idf:
            tf.append({line["ID"]: {x: idf[x] * line["Text"].count(x)}})