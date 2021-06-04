import csv
from nltk.corpus import stopwords

# lowercase
with open('./TrainingDS.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    entrada = dict()  # Diccionario para asignar id con su respectiva palabra
    next(csv_reader)

    for line in csv_reader:
        text = line[1].split(' ')
        NoStopWords = [x for x in text if not x in stopwords.words('english')]
        entrada["ID"] = line[0]
        entrada["Text"] = ' '.join(NoStopWords)
        entrada["Class"] = int(line[2])
        entrada["score_tag"] = line[3]
        entrada["agreement"] = line[4]
        entrada["subjectivity"] = line[5]
        entrada["confidence"] = line[6]
        entrada["irony"] = line[7]
        entrada["Happy"] = line[8]
        entrada["Fear"] = line[9]
        entrada["Sad"] = line[10]
        entrada["Bored"] = line[11]
        entrada["Angry"] = line[12]
        entrada["Excited"] = line[13]
        
        print(entrada["Text"])