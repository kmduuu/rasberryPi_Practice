
# Calculator

import tkinter as tk
from tkinter import messagebox
window = tk.Tk() # Create Tkinter Instance
window.title("계산기") # Window Name
window.geometry("450x400+200+200") # Tune WindowSize 
window.resizable(False, False) # Disabled WindowSize

def btn_click(item): # If you click Button,,, It works
    
    global expression
    expression = expression + str(item)
    input_text.set(expression)

    # / or * or + or - 중복 방지
    
    current = input_text.get()
  #  messagebox.showinfo("Current Value", current)
  #  messagebox.showinfo("item Value", item)
    
  #  if current.endswith("/") and item == "/":
  #      messagebox.showinfo("error", "error")
  #      pass
  #  else:
  #      input_text.set(current + str(item))

def bt_clear():
    global expression
    expression = ""
    input_text.set("")
    
def bt_equal():	
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = "" # Initialize Variable

input_text = tk.StringVar() # 



input_frame = tk.Frame(window, width=312, height=50, bd=0, background='black', highlightcolor='black', highlightthickness=2)
input_frame.pack(side='top')

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tk.Frame(window, width=312, height=272.5, bg='grey')
btns_frame.pack()

divide = tk.Button(btns_frame, text='/', fg='black', width=10, height=3, bd=0,
                   bg='#eee', cursor='hand2', command=lambda: btn_click('/'))
divide.grid(row=0, column=0, padx=1, pady=1)

clear = tk.Button(btns_frame, text='C', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda:bt_clear())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)  # 가로,세로 여백

clear = tk.Button(btns_frame, text='CLEAR', fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda:bt_clear())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)  # 가로,세로 여백

seven = tk.Button(btns_frame, text='7', fg='black', width=10, height=3, bd=0,
                  bg='#fff', cursor='hand2', command=lambda: btn_click(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = tk.Button(btns_frame, text='8', fg='black', width=10, height=3, bd=0,
                  bg='#fff', cursor='hand2', command=lambda: btn_click(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = tk.Button(btns_frame, text='9', fg='black', width=10, height=3, bd=0,
                 bg='#fff', cursor='hand2', command=lambda: btn_click(9))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = tk.Button(btns_frame, text='*', fg='black', width=10, height=3, bd=0,
                     bg='#fff', cursor='hand2', command=lambda: btn_click('*'))
multiply.grid(row=1, column=3, padx=1, pady=1)

four = tk.Button(btns_frame, text='4', fg='black', width=10, height=3, bd=0,
                 bg='#fff', cursor='hand2', command=lambda: btn_click(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = tk.Button(btns_frame, text='5', fg='black', width=10, height=3, bd=0,
                 bg='#fff', cursor='hand2', command=lambda: btn_click(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = tk.Button(btns_frame, text='6', fg='black', width=10, height=3, bd=0,
                bg='#fff', cursor='hand2', command=lambda: btn_click(6))
six.grid(row=2, column=2, padx=1, pady=1)

minus = tk.Button(btns_frame, text='-', fg='black', width=10, height=3, bd=0,
                  bg='#fff', cursor='hand2', command=lambda: btn_click('-'))
minus.grid(row=2, column=3, padx=1, pady=1)

one = tk.Button(btns_frame, text='1', fg='black', width=10, height=3, bd=0,
                bg='#fff', cursor='hand2', command=lambda: btn_click(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = tk.Button(btns_frame, text='2', fg='black', width=10, height=3, bd=0,
                bg='#fff', cursor='hand2', command=lambda: btn_click(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = tk.Button(btns_frame, text='3', fg='black', width=10, height=3, bd=0,
                  bg='#fff', cursor='hand2', command=lambda: btn_click(3))
three.grid(row=3, column=2, padx=1, pady=1)

plus = tk.Button(btns_frame, text='+', fg='black', width=10, height=3, bd=0,
                 bg='#fff', cursor='hand2', command=lambda: btn_click('+'))
plus.grid(row=3, column=3, padx=1, pady=1)

zero = tk.Button(btns_frame, text='0', fg='black', width=24, height=3, bd=0,
                 bg='#fff', cursor='hand2', command=lambda: btn_click(0))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = tk.Button(btns_frame, text='.', fg='black', width=10, height=3, bd=0,
                  bg='#fff', cursor='hand2', command=lambda: btn_click('.'))
point.grid(row=4, column=2, padx=1, pady=1)

equals = tk.Button(btns_frame, text='=', fg='black', width=10, height=3, bd=0,
                   bg='#fff', cursor='hand2', command=lambda: bt_equal())
equals.grid(row=4, column=3, padx=1, pady=1)

window.mainloop()
