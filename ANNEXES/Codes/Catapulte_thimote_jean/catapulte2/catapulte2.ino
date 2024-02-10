/*
   Code 23 - Edurobot.ch, destiné à l'Arduino
   Objectif : Faire bouger le bras d'un servomoteur dans un sens puis dans l'autre, indéfiniment
*/

//*****EN-TÊTE DECLARATIF*****
#include <Servo.h>  // on inclut la bibliothèque pour piloter un servomoteur
Servo moteur;
Servo monServo;
Servo servo1;
Servo bras;
Servo monServo2;  // on crée l'objet monServo
#define pinX    A2
#define pinY    A1
#define swPin    6
int Axe_X = A2;
int servoVal;

void setup()
{
    pinMode(2, INPUT);
    monServo.attach(9);
    bras.attach(12);
    monServo2.attach(3); // on définit le Pin utilisé par le servomoteur
    pinMode(pinX, INPUT);
    servo1.attach(12);
    pinMode (Axe_X, INPUT);
    moteur.attach(6);
}


void loop()
{
        if (digitalRead(2) == HIGH) {
          monServo2.write(0);  // le bras du servomoteur prend la position de la variable position
          delay(200);
          monServo2.write(90);
          delay(500);
          bras.write(0);
          delay(2000);
          monServo.write(0);
          delay(1000);
          bras.write(120);
          delay(1500);
          monServo.write(90);  // le bras du servomoteur prend la position de la variable position
          delay(500);  // on attend 15 millisecondes
          bras.write(90);
          delay(500);
        }
      servoVal = analogRead (Axe_X);
      servoVal = map(servoVal, 0, 1023, 900, 2100);
      moteur.writeMicroseconds(servoVal);
      delay(30);
}

    //for (int position = 90; position >=0; position --){ // cette fois la variable position passe de 180 à 0°
     //   monServo.write(position);  // le bras du servomoteur prend la position de la variable position
      //  delay(15);  // le bras du servomoteur prend la position de la variable position
    //}

