/**
 * Arduino framework
 * zakldy pouzivani
 */

// rikame, ze chceme pouzit knihovnu Arduino
#include <Arduino.h>

// Funkce setup se zavola jednou hned na zacatku.
void setup()
{
	// Nastavime pin s danym cislem (zde cislo 13) jako vystupni.
	// Vystupni zarizeni je to, ktere ovladame,
	// vstupni je to, ze ktereho cteme informaci.
	pinMode(13, OUTPUT);
}

// Funkce loop se provadi po skonceni funkce setup porad dokola.
void loop()
{
	// rozsvitime LEDku na pinu 13 tim, ze nastavime vystup na HIGH,
	// tedy logicka 1, tedy 5V (pripadne 3.3V na ESP)
	digitalWrite(13, HIGH);
	
	// pockame 1000ms, tedy 1s
	delay(1000);
	
	// zhasneme LEDku
	digitalWrite(13, LOW);
	
	// opet pockame 1000ms, aby LEDka zustala aspon chvili zhasnuta
	delay(1000);
}
