import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print ("Message received: "  + message.payload)
 
Connected = False   #global variable for the state of the connection
data1=1             # sending datas
data2=2
data3=3

broker_address= "soldier.cloudmqtt.com"  #Broker address
port = 13921                         #Broker port
user = "laoignzu"                    #Connection username
password = "8j4Fd0mw1Gw8"            #Connection password
 
client = mqttClient.Client()               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
    


while True:
    data = str(data1)+","+str(data2)+","+str(data3)+"\n"
    client.publish("computer",data)
    #data2 = str(data1+5)+","+str(data2+5)+","+str(data3+5)+"\n"
    #client.publish("esp",data2)
    print(data)
    #print(data2)
    data1 = data1 +1
    data3 = data1 +2
    data2 = data1 +3
    time.sleep(5)

client.loop_stop()
client.disconnect()
