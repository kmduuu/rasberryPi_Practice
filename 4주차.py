import tkinter as tk

# 윈도우 생성
window = tk.Tk()
window.title("My First Window")
window.geometry("400x400+200+200")
window.resizable(False, False)

# 라벨 생성
hello = tk.Label(
    text='Hello, Tkinter',
    fg='white',
    bg='black',
    width=10,
    height=5
)
hello.pack()  # Label을 윈도우에 배치

# 버튼 생성
button = tk.Button(
    text='Click me',
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)
button.pack()  # 버튼을 윈도우에 배치

# Entry
entry = tk.Entry(fg='black', bg='white', width=50)

def myInput(event):
    hello.config(text=entry.get())

entry.bind('<Return>', myInput)
entry.pack()

frame1 = tk.Frame(master=window, relief='sunken', bd=2)
frame2 = tk.Frame(master=window, relief='solid', bd=2)

label1 = tk.Label(master=frame1, text='I am in Frame1', height=3)
label1.pack()
label2 = tk.Label(master=frame2, text='I am in Frame2', height=6)
label2.pack()

# 윈도우 실행
window.mainloop()
