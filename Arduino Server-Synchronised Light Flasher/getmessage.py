#Script reaches across a server and pulls the String value to flash a light on the Arduino depending on value.

from mosquitto import *
from serial import *
from random import *

board = Serial("COM5",9600,timeout=2)
board.readall()


randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")
print("Connected")

client.subscribe("/lights")

def messageReceived(broker, obj, msg):
    #print("Message recieved")
    global client
    payload = msg.payload.decode()
    board.write(payload.encode() + '\n')
    print(payload.encode() + '\n')

client.on_message = messageReceived

while (client != None): client.loop()
