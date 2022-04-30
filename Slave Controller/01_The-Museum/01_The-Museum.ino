/*
Version | 2.00
License | WTFPL http://www.wtfpl.net/

Code written and designed by Elliott Hall
Project | The Museum

www.elliotthall.co.uk
@elliotth30 / @obscure_design
*/

//Libary Imports//

#include <ESP8266WiFi.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();


//Wireless Details//

const char AP_NameChar[] = "The Museum" ;
const char WiFiPassword[] = "";

WiFiServer server(80); // Setting Access Point Port


//Webpage Ingest \ HTML+CSS section//

String header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
String html_1 = "<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'/><meta charset='utf-8'><style>body {font-size:140%;} #main {display: table; margin: auto;  padding: 0 10px 0 10px; } h2,{text-align:center; } .button { padding:10px 10px 10px 10px; width:100%;  background-color: #61ede6; font-size: 120%;}</style><title>The Museum</title></head><body><div id='main'><h2>Museum Controller</h2><br><br>";
String html_2 = "<form id='F1' action='P1_ON'><input class='button' type='submit' value='<P1 Light ON' ></form><br>";
String html_3 = "<form id='F2' action='P1_OFF'><input class='button' type='submit' value='P1 Light OFF' ></form><br>";

String html_4 = "<form id='F2' action='P2_ON'><input class='button' type='submit' value='P2 Light ON' ></form><br>";
String html_5 = "<form id='F2' action='P2_OFF'><input class='button' type='submit' value='P2 Light OFF' ></form><br>";

String html_6 = "<form id='F2' action='P3_ON'><input class='button' type='submit' value='P3 Light ON' ></form><br>";
String html_7 = "<form id='F2' action='P3_OFF'><input class='button' type='submit' value='P3 Light OFF' ></form><br>";

String html_8 = "<form id='F2' action='P1_X_ON'><input class='button' type='submit' value='P1 Motor ON' ></form><br>";
String html_9 = "<form id='F2' action='P1_X_OFF'><input class='button' type='submit' value='P1 Motor OFF' ></form><br>";

String html_10 = "<form id='F2' action='P2_X_ON'><input class='button' type='submit' value='P2 Misc ON' ></form><br>";
String html_11 = "<form id='F2' action='P2_X_OFF'><input class='button' type='submit' value='P2 Mic OFF' ></form><br>";

String html_12 = "<form id='F2' action='P3_X_ON'><input class='button' type='submit' value='P3 Misc ON' ></form><br>";
String html_13 = "<form id='F2' action='P3_X_OFF'><input class='button' type='submit' value='P3 Misc OFF' ></form><br>";


String html_14 = "</div></body></html>";

String request = "";


//Variable Area//

int servonum = 15;
int pulselength;
String loops;



//Declaring View configurations//

// - Lighting

void P1_light_ON() {
  digitalWrite(5, HIGH);
  Serial.println("P1_light_ON");
}

void P1_light_OFF() {
  digitalWrite(5, LOW);
  Serial.println("P1_light_OFF");
}

void P2_light_ON() {
  digitalWrite(4, HIGH);
}

void P2_light_OFF() {
  digitalWrite(4, LOW);
}

void P3_light_ON() {
  digitalWrite(0, HIGH);
}

void P3_light_OFF() {
  digitalWrite(0, LOW);
}

// - Artefacts

void P1_Motor_ON() {
  digitalWrite(5, HIGH);
  Serial.println("P1_light_ON");
}

void P1_Motor_OFF() {
  digitalWrite(5, LOW);
  Serial.println("P1_light_OFF");
}

void P2_X_ON() {
  digitalWrite(4, HIGH);
}

void P2_X_OFF() {
  digitalWrite(4, LOW);
}

void P3_X_ON() {
  digitalWrite(0, HIGH);
}

void P3_X_OFF() {
  digitalWrite(0, LOW);
}

void setup() {
  
  Serial.begin(9600); // Debug over serial at 9600 baudrate

  boolean conn = WiFi.softAP(AP_NameChar, WiFiPassword); // Consolidate Wireless function for connection monitoring
  server.begin(); // Initialise the WebSerer (Soft AP)
}



//MAIN Code loop //
void loop() {
  //Button_Trigger();
  //delay(10);

  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client)  {  return;  }
  
  // Read the first line of the request
  request = client.readStringUntil('\r');
  
  if       ( request.indexOf("P1_ON") > 0 )  { P1_light_ON();  }
  else if  ( request.indexOf("P1_OFF") > 0 ) { P1_light_OFF();   }
  else if  ( request.indexOf("P2_ON") > 0 ) { P2_light_OFF();   }
  else if  ( request.indexOf("P2_OFF") > 0 ) { P2_light_OFF();   }
  else if  ( request.indexOf("P3_ON") > 0 ) { P3_light_OFF();   }
  else if  ( request.indexOf("P3_OFF") > 0 ) { P3_light_OFF();   }
  else if  ( request.indexOf("P1_X_ON") > 0 ) { P1_Motor_ON();   }
  else if  ( request.indexOf("P1_X_OFF") > 0 ) { P1_Motor_OFF();   }
  else if  ( request.indexOf("P2_X_ON") > 0 ) { P2_X_ON();   }
  else if  ( request.indexOf("P2_X_OFF") > 0 ) { P2_X_OFF();   }
  else if  ( request.indexOf("P3_X_ON") > 0 ) { P3_X_ON();   }
  else if  ( request.indexOf("P3_X_OFF") > 0 ) { P3_X_OFF();   }

  
  client.flush();
  
  client.print( header );
  client.print( html_1 );
  client.print( html_2 );
  client.print( html_3 );
  client.print( html_4 );
  client.print( html_5 );
  client.print( html_6 );
  client.print( html_7 );
  client.print( html_8 );
  client.print( html_9 );
  client.print( html_10 );
  client.print( html_11 );
  client.print( html_12 );
  client.print( html_13 );
  client.print( html_14 );
  
  
  delay(5);
}
