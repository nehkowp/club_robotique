int DIN_pin = 11;
int CS_pin = 10;
int CLK_pin = 12;
int rond[8] = {0x3c,0x42,0x81,0x81,0x81,0x81,0x42,0x3c}; 
int croix[8] = {0x81,0x42,0x24,0x18,0x18,0x24,0x42,0x81}; 
void write_pix(int data)
{
 	digitalWrite(CS_pin, LOW);
 	for (int i = 0; i < 8; i++)
 	{
 			digitalWrite(CLK_pin, LOW);
 			digitalWrite(DIN_pin, data & 0x80); // masquage de donnée
 			data = data << 1; // on décale les bits vers la gauche
 			digitalWrite(CLK_pin, HIGH);
 	}
}
void write_line(int adress, int data)
{
 	digitalWrite(CS_pin, LOW);
 	write_pix(adress);
 	write_pix(data);
 	digitalWrite(CS_pin, HIGH);
}
void write_matrix(int *tab)
{
 	for (int i = 0; i < 8; i++) write_line(i + 1, tab[i]);
}
void init_MAX7219(void)
{
 	write_line(0x09, 0x00); //decoding BCD
 	write_line(0X0A, 0x01); //brightness
 	write_line(0X0B, 0x07); //scanlimit 8leds
 	write_line(0X0C, 0x01); //power-down mode 0, normalmode1;
 	write_line(0X0F, 0x00);
}
void clear_matrix(void)
{
 	const int clean[8] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
 	write_matrix(clean);
}
int intToHex(int x)
{
 	switch (x)
 	{
 			case 0: return 0x01; break; //LED sur la première case
 			case 1: return 0x02; break; //LED sur 2 case
 			case 2: return 0x04; break; //LED sur 3 case
 			case 3: return 0x08; break; //LED sur 4 case
 			case 4: return 0x10; break; //LED sur 5 case
 			case 5: return 0x20; break; //LED sur 6 case
 			case 6: return 0x40; break; //LED sur 7 case
 			case 7: return 0x80; break; //LED sur 8 case
 	}
}

void setup()
{
 	pinMode(CS_pin, OUTPUT);
 	pinMode(DIN_pin, OUTPUT);
 	pinMode(CLK_pin, OUTPUT);
 	delay(50);
 	init_MAX7219();
 	clear_matrix();
}
void loop()
{
  write_matrix(rond);
  delay(500);
  write_matrix(croix);
  delay(500);

}