import tkinter as tk
window = tk.Tk()

button = tk.Button(text='Light is off', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
light = "off"
window.configure(bg="black")

def changeLight(event):
    global light
    global button
    light = "off" if light == "on" else "on"
    print("Light is turned off") if light == "off" else print("Light is turned on")
    button.configure(text='Light is off') if light == "off" else button.configure(text='Light is on')
    window.configure(bg="black") if light == "off" else window.configure(bg='yellow')

button.bind('<Button>', changeLight)


# schijf hier tussen je code

window.mainloop()