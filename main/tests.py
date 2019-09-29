from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import models
import paho.mqtt.client as mqttClient
import time


veriler = ["0","0" ,"0"]
data =0
veriler[0] ="0"
veriler[1] = "0"
veriler[2] = "0"

broker_address= "soldier.cloudmqtt.com"  
port = 13921                        
user = "laoignzu"                   
password = "8j4Fd0mw1Gw8"

def on_connect(client , userdata ,flags ,rc):
    print("Connecting with code : " ,rc )
    #Subscribe data..
    client.subscribe("computer/#")

def on_disconnect(client , userdata ,flags ,rc):
	client.loop_stop()

def on_message(client,userdata,msg):
	global data
	data = msg.payload
	datas = str(data)
	inx =len(datas)
	data = datas[2:(inx-3)]
	
def get_data_computer(request):
    client = mqttClient.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
	#client .connect(broker_address,port)
	#client.connect_async(broker_address, port, keepalive=60,bind_address="")
    client.connect_async(broker_address, port , keepalive=60 ,bind_address="" )
	#client.username_pw_set(user, password=password)   
    client.username_pw_set(user,password=password)
    client.loop_start()
    veriler= str(data).split(',')
    #Veri tabanına veri ekleme
    veri = models.Data_database(title='Ismet Taha',system_name ='Computer',data1=int(veriler[0]),data2=int(veriler[1]),data3=int(veriler[2]))
    veri.save()
    context = {
		'data1' : int(veriler[0]),
		'data2' : int(veriler[1]),
		'data3' : int(veriler[2])
	}
    return JsonResponse(context)