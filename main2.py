import csv
import string

with open('./TrainingDS.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    entrada = dict()  # Diccionario para asignar id con su respectiva palabra
    
    training = [] # Guarda diccionario entrada en una lista
    test = [] # Guarda diccionario entrada en una lista

    next(csv_reader)
    counter = 0
    for line in csv_reader:

        entrada["ID"] = int(line[0])
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
        entrada["Class"] = int(line[2])
        if counter < 1200:
            training.append(dict(entrada))
        else:
            test.append(dict(entrada))
        counter += 1

    with open('TrainingDS1.csv', 'w') as new_file:
        headers = ["ID", "score_tag", "agreement", "subjectivity", "confidence", "irony", "Happy", "Fear", "Sad", "Bored", "Angry", "Excited", "Class"]
    
        csv_writer = csv.DictWriter(new_file, fieldnames=headers)
        csv_writer.writeheader()

        for line in training:
            csv_writer.writerow(line)
    
    with open('TestDS1.csv', 'w') as new_file:
        headers = ["ID", "score_tag", "agreement", "subjectivity", "confidence", "irony", "Happy", "Fear", "Sad", "Bored", "Angry", "Excited", "Class"]
    
        csv_writer = csv.DictWriter(new_file, fieldnames=headers)
        csv_writer.writeheader()

        for line in test:
            csv_writer.writerow(line)