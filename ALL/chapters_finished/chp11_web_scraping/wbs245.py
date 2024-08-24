import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt') #DOWNLOADS THE FILE
res.raise_for_status()
playFile = open('RomeAndJuliet.txt', 'wb') #CALLS open() WITH 'wb' TO CREATE NEW FILE IN WRITE BINARY MODE
for chunk in res.iter_content(100000): #LOOP OVER THE 'RESPONSE' OBJECT'S iter_content() METHOD
    playFile.write(chunk) #CALL WRITE ON EACH ITERATION OF THE FILE

playFile.close() #CLOSES THE FILE WITH close()