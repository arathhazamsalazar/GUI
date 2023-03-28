import tkinter as tk
import subprocess

root = tk.Tk()
root.configure(background='black')  # establece el color de fondo negro

# Crea una etiqueta con texto verde claro
label = tk.Label(root, text="S4FB00T:1.0", fg='#7FFF00', bg="black", padx=10, pady=50)
label.pack()

# Crea un contenedor para los botones
button_frame = tk.Frame(root, bg='black')
button_frame.pack()

# Crea botones con texto blanco y agrégalo al contenedor
button1 = tk.Button(button_frame, text="R4ffleB00T", fg="white", bg="black")
button1.pack(side='left', padx=10)

def run_script():
    subprocess.run(['C:/oficial_S4FB00T1.0/GUI/PR00XYB0T/proxyALT.cmd'])

button2 = tk.Button(button_frame, text="Aplicar antes del Pr0xyB00T", fg="white", bg="black", command=run_script)
button2.pack(side='left', padx=10)

def run_script():
    subprocess.run(['C:/oficial_S4FB00T1.0/GUI/GUI/1use.bat'])

button3 = tk.Button(button_frame, text="Pr0xyB00T", fg="white", bg="black", command=run_script)
button3.pack(side='left', padx=10)

root.attributes('-fullscreen', True)  # abre la ventana en pantalla completa

root.mainloop()
