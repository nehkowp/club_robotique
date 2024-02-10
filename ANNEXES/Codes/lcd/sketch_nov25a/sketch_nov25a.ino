#include "Wire.h"
#include "LiquidCrystal_I2C.h"

LiquidCrystal_I2C LCD1(0x27, 16, 2); // définit le type d'ecran lcd 16 x 2

void setup() {
   LCD1.init(); // initialisation de l'afficheurs
    LCD1.backlight();
}

void loop() {
   LCD1.setCursor(1, 0);
   LCD1.print("ellimaC");
   LCD1.setCursor(3, 1);
   LCD1.print("ÏABAL");
   LCD1.scrollDisplayRight();
   delay(300);
}
