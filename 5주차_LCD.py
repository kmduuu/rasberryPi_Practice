from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# BCM pin numbers
lcd_rs = digitalio.DigitalInOut(board.D7)  # LCD pin 4
lcd_en = digitalio.DigitalInOut(board.D8)  # LCD pin 6
lcd_d4 = digitalio.DigitalInOut(board.D25)  # LCD pin 11
lcd_d5 = digitalio.DigitalInOut(board.D24)  # LCD pin 12
lcd_d6 = digitalio.DigitalInOut(board.D23)  # LCD pin 13
lcd_d7 = digitalio.DigitalInOut(board.D18)  # LCD pin 14

# Initialize the LCD class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

# Clear LCD screen
lcd.clear()
sleep(2)

print("Run...1")

run = 0;

while True:
    
    lcd_line1 = 'Hello World!'
    lcd_line2 = ''
    lcd.message = lcd_line1 + lcd_line2
    
    run = run+1
    print(run)
    sleep(2)
while False:
    print("Loser")
