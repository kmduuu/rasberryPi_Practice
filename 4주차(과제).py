# Practice 2

import tkinter as tk
from tkinter import messagebox 
import RPi.GPIO as GPIO
import time

print("Subject 4")

window = tk.Tk()
window.title("GPIO UI")
window.geometry("205x160+200+200")
# window.resizable(False, False)

# 1. Button Click!
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
# 2. button led ON!
def bt_led_on():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    out_field.config(text='LED ON')
    
def bt_led_off():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
    out_field.config(text='LED OFF')
    

input_frame = tk.Frame(window, width=205, height=50, bd=1, highlightbackground='black', highlightcolor='black', highlightthickness=2)
input_frame.pack(side='top')

out_field = tk.Label(text='LED CONTROL', fg='white', bg='black', width=50, height=3)
out_field.pack()

btns_frame = tk.Frame(window, width=205, height=100, bg='grey')
btns_frame.pack()

ledOn = tk.Button(btns_frame, text='LED ON', fg='black', width=13, height=6, bd=2, bg='#eee', cursor='hand2', command=lambda:bt_led_on())
ledOn.grid(row=0, column=0, padx=1, pady=1)

ledOff = tk.Button(btns_frame, text='LED OFF', fg='black', width=13, height=6, bd=2, bg='#eee', cursor='hand2', command=lambda:bt_led_off())
ledOff.grid(row=0, column=1, padx=1, pady=1)

window.mainloop()