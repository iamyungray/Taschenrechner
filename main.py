import tkinter as tk

# Funktionen für die Rechenoperationen
def addieren():
    result.set(num1.get() + num2.get())

def subtrahieren():
    result.set(num1.get() - num2.get())

def multiplizieren():
    result.set(num1.get() * num2.get())

def dividieren():
    try:
        result.set(num1.get() / num2.get())
    except ZeroDivisionError:
        result.set("Division durch Null nicht erlaubt.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")
root.configure(bg='#252525')  # schwarzer Hintergrund

# Eingabefelder erstellen
num1 = tk.DoubleVar()
num2 = tk.DoubleVar()

entry_num1 = tk.Entry(root, textvariable=num1, font=('Arial', 14), bd=0, bg='#555555', fg='white')
entry_num1.pack(side=tk.LEFT, padx=10, pady=10)

entry_num2 = tk.Entry(root, textvariable=num2, font=('Arial', 14), bd=0, bg='#555555', fg='white')
entry_num2.pack(side=tk.LEFT, padx=10, pady=10)

# Button-Widgets erstellen
add_button = tk.Button(root, text="+", font=('Arial', 14), command=addieren, bd=0, bg='#555555', fg='white', activebackground='#333333', activeforeground='white')
add_button.pack(side=tk.LEFT, padx=10, pady=10)

sub_button = tk.Button(root, text="-", font=('Arial', 14), command=subtrahieren, bd=0, bg='#555555', fg='white', activebackground='#333333', activeforeground='white')
sub_button.pack(side=tk.LEFT, padx=10, pady=10)

mul_button = tk.Button(root, text="*", font=('Arial', 14), command=multiplizieren, bd=0, bg='#555555', fg='white', activebackground='#333333', activeforeground='white')
mul_button.pack(side=tk.LEFT, padx=10, pady=10)

div_button = tk.Button(root, text="/", font=('Arial', 14), command=dividieren, bd=0, bg='#555555', fg='white', activebackground='#333333', activeforeground='white')
div_button.pack(side=tk.LEFT, padx=10, pady=10)

# Ausgabe-Label erstellen
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Arial', 16), bg='#252525', fg='white')
result_label.pack(side=tk.LEFT, padx=10, pady=10)

# Hauptfenster starten
root.mainloop()
