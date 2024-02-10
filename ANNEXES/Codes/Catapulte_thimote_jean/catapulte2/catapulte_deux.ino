/*
   Code 23 - Edurobot.ch, destiné à l'Arduino
   Objectif : Faire bouger le bras d'un servomoteur dans un sens puis dans l'autre, indéfiniment
*/

//*****EN-TÊTE DECLARATIF*****
#include <Servo.h>  // on inclut la bibliothèque pour piloter un servomoteur
Servo direction;
Servo bloqueur;
Servo servo;
Servo lebras;
Servo reserve;  // on crée l'objet monServo
#define pinX    A2
#define pinY    A1
#define swPin    7
int Axe_x = A2;
int servoval;

void setup()
{
    pinMode(2, INPUT);
    bloqueur.attach(9);
    lebras.attach(12);
    reserve.attach(3); // on définit le Pin utilisé par le servomoteur
    pinMode(pinX, INPUT);
    pinMode (Axe_x, INPUT);
    direction.attach(6);
}
  

void loop()
{
        if (digitalRead(2) == HIGH) {
          reserve.write(0);  // le bras du servomoteur prend la position de la variable position
          delay(200);
          reserve.write(90);
          delay(500);
          lebras.write(0);
          delay(2000);
          bloqueur.write(0);
          delay(1000);
          lebras.write(120);
          delay(1500);
          bloqueur.write(90);  // le bras du servomoteur prend la position de la variable position
          delay(500);  // on attend 15 millisecondes
          lebras.write(90);
          delay(500);
        }
      servoval = analogRead (Axe_x);
      servoval = map(servoval, 0, 1023, 900, 2100);
      direction.writeMicroseconds(servoval);
      delay(30);
}

    //for (int position = 90; position >=0; position --){ // cette fois la variable position passe de 180 à 0°
     //   monServo.write(position);  // le bras du servomoteur prend la position de la variable position
      //  delay(15);  // le bras du servomoteur prend la position de la variable position
    //}

