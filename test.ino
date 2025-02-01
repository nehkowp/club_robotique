// Définition des pins de connexion
int DIN_pin = 11; // Data In
int CS_pin = 10;  // Chip Select
int CLK_pin = 12; // Clock

// Fonction pour envoyer un octet de données au MAX7219
void write_pix(int data) {
  for (int i = 0; i < 8; i++) {
    digitalWrite(CLK_pin, LOW);
    digitalWrite(DIN_pin, (data & 0x80) ? HIGH : LOW); // Envoi du bit le plus significatif
    data = data << 1; // Décalage des bits
    digitalWrite(CLK_pin, HIGH);
  }
}

// Fonction pour écrire sur une ligne donnée de toutes les matrices
void write_line(int address, int data) {
  digitalWrite(CS_pin, LOW);
  for (int i = 0; i < 4; i++) { // 4 matrices
    write_pix(address); // Envoi de l'adresse (ligne 1 à 8)
    write_pix(data);    // Envoi de la donnée pour cette ligne
  }
  digitalWrite(CS_pin, HIGH);
}

// Fonction d'initialisation du MAX7219
void init_MAX7219() {
  write_line(0x09, 0x00); // Mode de décodage : Aucun
  write_line(0x0A, 0x08); // Luminosité moyenne
  write_line(0x0B, 0x07); // Activation des 8 lignes
  write_line(0x0C, 0x01); // Mode normal (sortie de veille)
  write_line(0x0F, 0x00); // Désactivation du mode test
}

// Fonction pour nettoyer toutes les matrices
void clear_matrix() {
  for (int i = 1; i <= 8; i++) {
    write_line(i, 0x00); // Éteint toutes les LEDs
  }
}

void setup() {
  pinMode(CS_pin, OUTPUT);
  pinMode(DIN_pin, OUTPUT);
  pinMode(CLK_pin, OUTPUT);

  digitalWrite(CS_pin, HIGH);
  delay(50);

  init_MAX7219();
  clear_matrix();
}

// Boucle de test : allume progressivement les LEDs
void loop() {
  for (int i = 1; i <= 8; i++) {
    write_line(i, 0xFF); // Allume la ligne `i` sur toutes les matrices
    delay(300);
  }
  delay(1000);
  clear_matrix();
  delay(1000);
}
