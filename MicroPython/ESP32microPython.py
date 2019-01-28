# Dokumentace k tomuto tématu podrobně v angličtině dostupná na:
# https://docs.micropython.org/en/latest/esp32/quickref.html

# MicroPython na ESP32 běží jako aplikace napsaná v jazyce C++, kterou si na Robotárně upravujeme podle vlastních potřeb. Po připojení ESP32 k počítači přes USB se automaticky spustí interpret jazyka Python. Příkazy a programy napsané v jazyce Python se do čipu ESP32 nahrávají pomocí sériové linky řpipojené právě USB kabelem k počítači. Nyní si vyzkoušíme posílání příkazů v jazyce Python do ESP32 a později si zkusíme čip ESP32 naprogramovat přímo v jazyce C++. Nyní si vyzkoušíme interaktivní posílání příkazů v jazyce Python:

# Příkaz help() vám zobrazí nápovědu v angličtině, doporučuji přečíst
help()

# Pokud chceme pracovat se vstupy a výstupy (GPIO), musíme nejprve importovat modul machine
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
