#include <SPI.h>
#include <LoRa.h>

int LED = 3;
String inString = "";
int val = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  while (!Serial);

  Serial.println("LoRa Receiver");
  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    while (LoRa.available()) {
      inString += (char)LoRa.read();
      val = inString.toInt();
    }
    inString = "";
  }
  Serial.println(val);
  analogWrite(LED, val);
}
