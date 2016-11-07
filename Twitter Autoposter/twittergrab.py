import twitter
import sqlite3
import datetime

file = open("keys.txt")
creds = file.read().split('\n')
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
history = sqlite3.connect("C:\Users\charlotte\AppData\Local\Google\Chrome\User Data\Default\History")
cursor = history.cursor()
cursor.execute("SELECT urls.title, datetime(visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') FROM urls, visits WHERE urls.id = visits.url;")
rows = cursor.fetchall()

rowarray = []

for row in rows:
    rowarray.append(row)
    

data = str(rowarray[-1]).split("', u'")
data[0] = data[0].replace("(u'", "")
data[1] = data[1].replace("')", "")
date = data[1].split(" ")[0]
time = data[1].split(" ")[1]
data[1] = date
data.append(time)

currentH = datetime.datetime.now()
currentH = currentH.hour

while True:
    ct = datetime.datetime.now()
    if(ct.hour != currentH):
        currentH = ct.hour
        response = api.PostUpdate("Visited " + str(data[0]) + " at " + str(data[2]) + " on " + str(data[1]))
        print("Status updated to: " + response.text)
        
#print(currentH)