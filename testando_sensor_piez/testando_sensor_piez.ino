int const sensor = A0; //declaração do sensor do tipo inteiro
int frequencia = 0; // frequência
long intervalo = 1000; //tempo em milisegundos 
long tempo_atual;
void setup() {
  Serial.begin(9600); //inicialização do monitor Serial
  pinMode(sensor, INPUT); // inicialização do sensor piezoeletrico
}

void loop() {
  int vibracao = analogRead(A0); 
  digitalWrite(2, vibracao);  
  if((millis() - tempo_atual) >= intervalo && frequencia > 0){ //condicional da qual verificará se a frequencia é maior do que 0 e se o tempo bateu 1 segundo
    frequencia = 0; //zera a frequência
  }
  if(vibracao > 150){
    if(frequencia == 0){
      tempo_atual = millis(); //inicializa o tempo
      }
    frequencia++;
    Serial.println(frequencia);
    delay(68); //delay que serve para a vibração parar no tempo certo
  }
}
