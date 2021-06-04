import paralleldots
import requests
import csv
import time

#Keys
api_key = "hh2Q5HhJ8ZhaaszPBWKZErjajHIvIRzGayVGKuKxblI"
api_key2 = "pDfSqjVZk7s5yeBk9fkTzyB3PH5qjn1AEvD1Z6FSmyg"

keyMC = '269d63b79389f23d64c62609e53c942f'

paralleldots.set_api_key( api_key ) # Asignacion de key1

#CSV read
with open('TrainingDS.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    # Headers
    headers = ['ID', 'Text', 'Class', 'score_tag', 'agreement', 'subjectivity', 'confidence', 'irony', 'Happy', 'Fear', 'Sad', 'Bored', 'Angry', 'Excited']
    
    with open('newDS.csv', 'w') as newfile:
        csv_writer = csv.DictWriter(newfile, fieldnames = headers)
        csv_writer.writeheader()
        
        credits=0 # Credits used 
        for line in csv_reader:
            # # Control # #
            time.sleep(3) # Delay to control the rate limit
            
            if credits >= 700:
                paralleldots.set_api_key( api_key2 ) # Asignacion de key2
            credits+=1
            
            # # Request # #
            # MeaningCloud Request
            sentiment = requests.post('https://api.meaningcloud.com/sentiment-2.1', data= {'key':keyMC, 'of':'json', 'lang':'en', 'model':'general', 'txt':line['Text']})
            # ParallelDots Request
            emotion = paralleldots.emotion(line['Text'])
            
            # Actualizar diccionario
            line[headers[3]] = sentiment.json()[headers[3]]
            line[headers[4]] = sentiment.json()[headers[4]]
            line[headers[5]] = sentiment.json()[headers[5]]
            line[headers[6]] = sentiment.json()[headers[6]]
            line[headers[7]] = sentiment.json()[headers[7]]
            line[headers[8]] = emotion['emotion'][headers[8]]
            line[headers[9]] = emotion['emotion'][headers[9]]
            line[headers[10]] = emotion['emotion'][headers[10]]
            line[headers[11]] = emotion['emotion'][headers[11]]
            line[headers[12]] = emotion['emotion'][headers[12]]
            line[headers[13]] = emotion['emotion'][headers[13]]

            print('{} {}'.format(sentiment.json()['status']['msg'], line))

            # Escribir linea
            csv_writer.writerow(line)
