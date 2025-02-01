// Définition des pins
int DIN_pin = 11; // Data In
int CS_pin = 10;  // Chip Select
int CLK_pin = 12; // Clock

// Motifs à afficher
int rond[8] = {0x3C, 0x42, 0x81, 0x81, 0x81, 0x81, 0x42, 0x3C}; 
int croix[8] = {0x81, 0x42, 0x24, 0x18, 0x18, 0x24, 0x42, 0x81}; 

// Fonction pour envoyer un octet de données au MAX7219
void write_pix(int data) {
  for (int i = 0; i < 8; i++) {
    digitalWrite(CLK_pin, LOW);
    digitalWrite(DIN_pin, (data & 0x80) ? HIGH : LOW); // Envoi du bit le plus significatif
    data = data << 1; // Décalage des bits
    digitalWrite(CLK_pin, HIGH);
  }
}

// Fonction pour écrire sur une ligne spécifique de chaque matrice
void write_matrix(int *tab1, int *tab2, int *tab3, int *tab4) {
  for (int i = 0; i < 8; i++) {
    digitalWrite(CS_pin, LOW);

    write_pix(i + 1); write_pix(tab4[i]); // 4ᵉ matrice (la dernière dans la chaîne)
    write_pix(i + 1); write_pix(tab3[i]); // 3ᵉ matrice
    write_pix(i + 1); write_pix(tab2[i]); // 2ᵉ matrice
    write_pix(i + 1); write_pix(tab1[i]); // 1ʳᵉ matrice (proche de l’Arduino)

    digitalWrite(CS_pin, HIGH);
  }
}

// Fonction pour initialiser le MAX7219
void init_MAX7219() {
  write_matrix(rond, rond, rond, rond); // Allume un motif pour vérifier
  delay(500);
  write_matrix(croix, croix, croix, croix); // Change le motif
  delay(500);
  clear_matrix();
}

// Fonction pour nettoyer toutes les matrices
void clear_matrix() {
  int clean[8] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
  write_matrix(clean, clean, clean, clean);
}

void setup() {
  pinMode(CS_pin, OUTPUT);
  pinMode(DIN_pin, OUTPUT);
  pinMode(CLK_pin, OUTPUT);

  digitalWrite(CS_pin, HIGH);
  delay(50);

  init_MAX7219();
}

void loop() {
  write_matrix(rond, croix, rond, croix);
  delay(500);
  write_matrix(croix, rond, croix, rond);
  delay(500);
}
