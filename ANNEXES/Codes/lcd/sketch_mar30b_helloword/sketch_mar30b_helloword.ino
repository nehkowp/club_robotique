#include "LiquidCrystal_I2C.h"
LiquidCrystal_I2C LCD(0x27, 16, 2);
 
void setup() {
   LCD.init();
   LCD.backlight();

   LCD.setCursor(2, 0);
   LCD.print("HELLO");
  
   LCD.setCursor(9, 1);
   LCD.print("WORLD");
}
 
void loop() {

}