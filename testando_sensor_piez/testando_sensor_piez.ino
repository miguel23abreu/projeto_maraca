#include <ESP8266WiFi.h>
#include <WiFiUDP.h>
#include <MIDI.h>

MIDI_CREATE_DEFAULT_INSTANCE();
const char* ssid = "Aifon";     // Nome da rede Wi-Fi do Arduino
const char* password = "miguel23abreu";   // Senha para a rede Wi-Fi do Arduino
const int port = 5006;              // Porta UDP que será usada
WiFiUDP udp;

int const sensor = A0; //declaração do sensor do tipo inteiro
int frequencia = 0; // frequência
long intervalo = 1000; //tempo em milisegundos 
long tempo_atual;
void setup() {
  Serial.begin(115200); //inicialização do monitor Serial
  pinMode(sensor, INPUT); // inicialização do sensor piezoeletrico
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    Serial.println("connecting to wifi...");
    delay(500);
  }

  Serial.println("wifi conectado"); 
  Serial.println(WiFi.localIP());
  udp.begin(port);
  //MIDI.begin(MIDI_CHANNEL_OMNI); //ao declarar o MIDI o monitor serial envia caracteres estranhos
}

void loop() {
  int packetSize = udp.parsePacket(); //verifica se há um pacote udp recebido e o amarzena 
  udp.beginPacket(udp.remoteIP(), port); //inicia um novo pacote udp
  int vibracao = analogRead(A0);
  int Dado_MIDI = map(vibracao, 0, 1023, 0, 127); 
  digitalWrite(2, vibracao);  
  if((millis() - tempo_atual) >= intervalo && frequencia > 0){ //condicional da qual verificará se a frequencia é maior do que 0 e se o tempo bateu 1 segundo
    frequencia = 0; //zera a frequência
  }
  if(vibracao > 150){
    if(frequencia == 0){
      tempo_atual = millis(); //inicializa o tempo
      }
    frequencia++;
    //MIDI.sendControlChange(1, Dado_MIDI, 1);
    Serial.println(frequencia);
    Serial.println(WiFi.localIP());
    udp.beginPacket("172.20.10.10", port); // Substitua "IP_DO_SEU_PC" pelo endereço IP do seu computador Python
    udp.write(frequencia); // Envia a frequência via UDP
    udp.write(Dado_MIDI); //Envia o dado MIDI para o algoritmo python 
    delay(68); //delay que serve para a vibração parar no tempo certo
  }
  udp.endPacket();
}
