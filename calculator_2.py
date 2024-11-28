import tkinter as tk

window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=5, height=3)
button_add.place(x=20, y=300)
button_sub = tk.Button(window, text='-', width=5, height=3)
button_sub.place(x=120, y=300)
button_myl = tk.Button(window, text='x', width=5, height=3)
button_myl.place(x=220, y=300)
button_div = tk.Button(window, text=':', width=5, height=3)
button_div.place(x=320, y=300)

number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=50, y=50)
number2_entry = tk.Entry(window, width=50)
number2_entry.place(x=50, y=100)
answer_entry = tk.Entry(window, width=50)
answer_entry.place(x=50, y=200)

number1 = tk.Label(window, text='Первое число')
number1.place(x=50, y=20)
number2 = tk.Label(window, text='Второе число')
number2.place(x=50, y=75)
answer = tk.Label(window, text='Сумма')
answer.place(x=50, y=170)

window.mainloop()