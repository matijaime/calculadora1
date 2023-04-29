import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Pantalla
        self.screen = tk.Entry(master, width=30, justify="right")
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Botones
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Función para agregar un número o operador a la pantalla
        def add_to_screen(value):
            current = self.screen.get()
            self.screen.delete(0, tk.END)
            self.screen.insert(0, str(current) + str(value))

        # Función para borrar la pantalla
        def clear_screen():
            self.screen.delete(0, tk.END)

        # Función para evaluar la expresión en pantalla
        def evaluate():
            expression = self.screen.get()
            result = str(eval(expression))
            self.screen.delete(0, tk.END)
            self.screen.insert(0, result)

        # Agregar botones a la calculadora
        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                tk.Button(master, text=button, width=7, height=3, command=evaluate).grid(row=row, column=col)
            elif button == "0":
                tk.Button(master, text=button, width=7, height=3, command=lambda: add_to_screen(0)).grid(row=5, column=1)
            elif button == ".":
                tk.Button(master, text=button, width=7, height=3, command=lambda: add_to_screen(".")).grid(row=5, column=2)
            elif button in ["+", "-", "*", "/"]:
                tk.Button(master, text=button, width=7, height=3, command=lambda value=button: add_to_screen(value)).grid(row=row, column=3)
            else:
                tk.Button(master, text=button, width=7, height=3, command=lambda value=button: add_to_screen(value)).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Botón de borrar
        tk.Button(master, text="Borrar", width=7, height=3, command=clear_screen).grid(row=5, column=0)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
