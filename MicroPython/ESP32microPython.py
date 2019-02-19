# Dokumentace k tomuto tématu podrobně v angličtině dostupná na:
# https://docs.micropython.org/en/latest/esp32/quickref.html

# MicroPython na ESP32 běží jako aplikace napsaná v jazyce C++, kterou si na Robotárně upravujeme podle vlastních potřeb. Po připojení ESP32 k počítači přes USB se automaticky spustí interpret jazyka Python. Příkazy a programy napsané v jazyce Python se do čipu ESP32 nahrávají pomocí sériové linky řpipojené právě USB kabelem k počítači. Nyní si vyzkoušíme posílání příkazů v jazyce Python do ESP32 a později si zkusíme čip ESP32 naprogramovat přímo v jazyce C++. Nyní si vyzkoušíme interaktivní posílání příkazů v jazyce Python:

# Příkaz help() vám zobrazí nápovědu v angličtině, doporučuji přečíst
help()

# Pro práci s periferiemi ALKS je nutné procesoru říct, že je připojen k ALKS a importovat vhodnou knihovnu s definicemi jednotlivých příkazů použitých níže
import alks

# Nejprve je třeba nastavit všechny piny (nožičky) procesoru na vstupní nebo výstupní nebo k nim přiřadit správnou periferii podle toho, k čemu jsou připojené. V případě ALKS to můžeme udělat zavoláním funkce:
alks.setupAll()

# Nyní můžeme otestovat, jestli je všechno správně a LEDky blikají:
alks.testLeds()

# Můžeme přidat interval blikání v milisekundách jako parametr funkce testLeds():
alks.testLeds(500)

# Rozsvěcování a zhasínání jednotlivých LED provádíme pomocí funkcí "on()" a "off()", případně "value(1)" odpovídá "on()" a "value(0)" odpovídá "off()". Jednotlivé LED jsou reprezentovány počátečními písmeny svých barev:
alks.r.on()
alks.r.off()
alks.g.on()
alks.g.off()
alks.b.on()
alks.b.off()
alks.y.on()
alks.y.off()
alks.RGBr.on()
alks.RGBg.on()
alks.RGBb.on()
alks.g.value(1)

# Poznámka: Pokud místo "import alks" napíšeme:
from alks import *
# tak nebudeme muset při každém zavolání libovolné funkce z knihovny ALKS psát "alks.jméno_funkce()":
setupAll()

# Pokud chceme používat jen některé periferie, nemusíme volat funkci "setupAll()", ale jen její části:
setupLeds()
setupRgbLeds()
setupButtons()
setupPiezo()

# Za chvíli budeme potřebovat funkci, která jen čeká nějaký zadaný čas v milisekundách:
alks.delay(1000)

# Pokud chceme, aby se příkazy vykonávaly pořád dokola, využijeme cyklus, který jsme se učili dříve:
# Terminál vás v tomto případě nechá vypsat více řádků. Pro ukončení je třeba na posledním řádku stisknout backspace a potom enter.
while True:
	r.on()
	delay(500)
	r.off()
	delay(500)

# Příklad: Naprogramuje semafor pro auta.

# Míchání barev pomocí RGB LED:
# Opět nejprve musíme procesoru říct, na kterých pinech je RGB LED připojená a že umí měnit svůj jas:
alks.setupRgbPwm()

# Barvy nastavujeme mícháním ze tří základních barev (červená - Red, zelená - Green, modrá - Blue). Například bílou barvu získáme takto smícháním všech tří zákaldních barev dohromady:
alks.RGBr.duty(1023)
alks.RGBg.duty(1023)
alks.RGBb.duty(1023)

# Všiměte si, že číslo 1023 nastavuje jas dané barvy a může nabývat hodnot od 0 (nesvítí vůbec) do 1023 (svítí naplno).

# Příklad: Jakou barvu namícháme pomocí těchto příkazů?
alks.RGBr.duty(512)
alks.RGBg.duty(256)
alks.RGBb.duty(128)

# Příklad: Vytvořte program, který zajistí postupné stmívání a rozsvěcování nějaké barvy na RGB LED.

# WiFi: ALKS obsahuje i WiFi modul, který můžete nastavit jako stanici nebo jako AccessPoint. Informace k tomu, jak WiFi používat si zkuste najít sami pomocí strýčka Google. Zde vám přidám jen malou nápovědu:
import network
wlan = network.WLAN(network.AP_IF)
wlan.active(True)
wlan.config("JmenoWiFi","heslo")
wlan.ifconfig()
... :)


## Pokročilé:

# Pokud chceme pracovat se vstupy a výstupy (GPIO) obecně, musíme nejprve importovat modul machine
import machine

# Pokud chceme pracovat s WiFi, potřebujeme modul metwork
import network

# Nejprve musíme proceosru ESP32 říct, na kterém pinu má připojenou kterou součástku
# To si uložíme například do proměnné "r" (jméno si zvolte dle libosti), červená LED je na pinu 22 a LED je výstupní zařízení
r = machine.Pin(22, machine.Pin.OUT)
g = machine.Pin(17, machine.Pin.OUT)
b = machine.Pin(5, machine.Pin.OUT)
y = machine.Pin(23, machine.Pin.OUT)
RGBr = machine.Pin(4, machine.Pin.OUT)
RGBg = machine.Pin(21, machine.Pin.OUT)
RGBb = machine.Pin(16, machine.Pin.OUT)

# Pokud chcete zavolat znovu předchozí příkaz, stačí stisknout šipku nahoru.
# Terminál zde funguje stejně jako linuxový terminál.

# LEDku rozsvítíme nebo zhasneme posláním logické 1 nebo 0 na daný pin.
r.value(1)
r.value(0)

# Příklad: Postupně rozsviťte a následně zhasněte všechny LEDky na ALKS.

# Čekání: Pokud budeme volat více příkazů hned za sebou, bude se nám hodit příkaz čekej. K tomu potřebujeme importovat modul time
import time

# Čekej 1 s = 1000 ms = 1000000 us
time.sleep_ms(1000)
time.sleep_us(1000000)

# Blikání s LEDkou: K tomu budeme potřebovat cyklus, který jsme se učili dříve.
# Terminál vás v tomto případě nechá vypsat více řádků. Pro ukončení je třeba na posledním řádku stisknout backspace a potom enter.
while True:
	r.value(1)
	time.sleep_ms(500)
	r.value(0)
	time.sleep_ms(500)

# Příklad: Naprogramuje semafor pro auta.

# Poznámka: Stejně jako LEDky můžeme používat tlačítka a další součástky na ALKS. Tlačítka jsou na pinech:
sw1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
sw2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
sw3 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Přečtení hodnoty na tlačítku
sw1.value()

# Piezo reproduktor je na pinech 18 a 19.
# Piezo ovládáme pomocí PWM
piezo = machine.PWM(machine.Pin(19))
piezo.duty(50)
# 440 Hz je frekvence tónu A1
piezo.freq(440)
