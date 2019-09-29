#include <stdio.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "TP-Link_E5F8";                   // wifi ssid
const char* password =  "23276154";         // wifi password
const char* mqttServer = "soldier.cloudmqtt.com";    // IP adress Raspberry Pi
const int mqttPort = 13921;
const char* mqttUser = "laoignzu";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "8j4Fd0mw1Gw8";  // if you don't have MQTT Password, no need input
char data[50];
int data1=0;
int data2=0;
int data3=0;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {

  Serial.begin(115200);
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {

      Serial.println("connected");

    } else {

      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);

    }
  }

//  client.publish("esp8266", "Hello Raspberry Pi");
//  client.subscribe("esp");

}

void callback(char* topic, byte* payload, unsigned int length) {

  Serial.print("Message arrived in topic: ");
  Serial.println(topic);

  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }

  Serial.println();
  Serial.println("-----------------------");

}

void loop() {
    data1 = data1+1;
    data2 = data2+2;
    data3 = data3+3;
    sprintf(data, "%d,%d,%d\n", data1,data2,data3);
    client.publish("esp", data);
    //client.subscribe("esp8266");
    delay(2000);
  client.loop();
}
