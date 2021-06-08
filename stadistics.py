import csv
import statistics

with open('./TrainingDS.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    entrada = dict()  # Diccionario para asignar id con su respectiva palabra
    saveIn = [] # Guarda diccionario entrada en una lista
    
    next(csv_reader)
    suma = 0
    for line in csv_reader:
        entrada[line[1]] = len(line[1].split())
        suma += len(line[1].split())
        # saveIn.append(dict(entrada))
    
    data = list(entrada.values())
    print("Desviación Estandar:", statistics.stdev(data))
    print("Media:", suma/len(entrada))