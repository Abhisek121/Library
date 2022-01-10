#include <WiFiManager.h> 
#include <ESP8266WiFi.h>     //Include Esp library
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <SPI.h>
#include <MFRC522.h>        //include RFID library
//
#define SS_PIN D2 //RX slave select
#define RST_PIN D1
#define RedLed D8
#define GreenLed D0
#define BlueLed D3
#define WaitLed D4
WiFiClient wifiClient;
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.

const char* ssid = "TP-LINK_62A4";
const char* pwd = "WiFiOfThanos";

String getData ,Link;
String CardID="";

void setup() {
  pinMode(GreenLed,OUTPUT);
  pinMode(BlueLed,OUTPUT);
  pinMode(RedLed,OUTPUT);
  pinMode(WaitLed,OUTPUT);
  digitalWrite(GreenLed,HIGH);
  delay(1000);
  digitalWrite(GreenLed,LOW);
  Serial.begin(115200);
  WiFi.begin(ssid, pwd);
  Serial.print("Connecting... ");
  
  while(WiFi.status()!= WL_CONNECTED){
    delay(500);
    Serial.print("Waiting... ");
  }
  SPI.begin();  // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card
  digitalWrite(RedLed,HIGH);
  //digitalWrite(BlueLed,HIGH);
  digitalWrite(WaitLed,HIGH);
  
  
  digitalWrite(WaitLed,LOW);
  digitalWrite(RedLed,LOW);
  //digitalWrite(BlueLed,LOW);
  Serial.println("CONNECTED!!");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP
  
}

void loop() {
//  if(WiFi.status() != WL_CONNECTED){
//    WiFiManager wifiManager;
//    digitalWrite(RedLed,HIGH);
//    //digitalWrite(BlueLed,HIGH);
//    digitalWrite(WaitLed,HIGH);
//    Serial.print("Setting up the wifi");
//    wifiManager.autoConnect("Avi","12345");
//    digitalWrite(WaitLed,LOW);
//    digitalWrite(RedLed,LOW);
//    //digitalWrite(BlueLed,LOW);
//    Serial.println("CONNECTED!!");
//    Serial.print("IP address: ");
//    Serial.println(WiFi.localIP());  //IP address assigned to your ESP
//  }
  
  //look for new card
   if ( ! mfrc522.PICC_IsNewCardPresent()) {
  return;//got to start of loop if there is no card present
 }
 // Select one of the cards
 if ( ! mfrc522.PICC_ReadCardSerial()) {
  return;//if read card serial(0) returns 1, the uid struct contians the ID of the read card.
 }

 for (byte i = 0; i < mfrc522.uid.size; i++) {
     CardID += mfrc522.uid.uidByte[i];
     }
  digitalWrite(WaitLed,HIGH);
  Serial.println("Remove your card and wait!");
  delay(700);
  Serial.println(CardID);     //Print Card ID
  HTTPClient http;    //Declare object of class HTTPClient
  
  //GET Data
  getData = CardID;
  Link = "http://192.168.0.105:8000/process/?card_id="+ getData; // ENTER YOUR HOST NAME HERE
  
  
  http.begin(wifiClient, Link);
  int httpCode = http.GET();            //Send the request
  delay(10);
  String payload = http.getString();    //Get the response payload
  
  Serial.println(httpCode);   //Print HTTP return code
  Serial.println(payload);    //Print request response payload
  
  if(payload == "login"){
    digitalWrite(WaitLed,LOW);
    digitalWrite(GreenLed,HIGH);
    Serial.println("green on");
    delay(1000); 
  }
  else if(payload == "logout"){
    digitalWrite(WaitLed,LOW);
    digitalWrite(BlueLed,HIGH);
    Serial.println("Blue on");
    delay(100);
  }
  else{
    digitalWrite(WaitLed,LOW);
    digitalWrite(RedLed,HIGH);
    delay(500);  
    }
  delay(500);
  
  CardID = "";
  getData = "";
  Link = "";
  http.end();  //Close connection
  digitalWrite(WaitLed,LOW);
  digitalWrite(GreenLed,LOW);
  digitalWrite(BlueLed,LOW);
  digitalWrite(RedLed,LOW);
}