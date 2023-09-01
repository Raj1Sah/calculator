import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        input_temp = float(entry_temp.get())
        from_unit = combo_from_unit.get()
        to_unit = combo_to_unit.get()

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result.set(f"{input_temp * 9/5 + 32:.2f} °F")
            elif to_unit == "Kelvin":
                result.set(f"{input_temp + 273.15:.2f} K")
            else:
                result.set(f"{input_temp:.2f} °C")
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result.set(f"{(input_temp - 32) * 5/9:.2f} °C")
            elif to_unit == "Kelvin":
                result.set(f"{(input_temp - 32) * 5/9 + 273.15:.2f} K")
            else:
                result.set(f"{input_temp:.2f} °F")
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result.set(f"{input_temp - 273.15:.2f} °C")
            elif to_unit == "Fahrenheit":
                result.set(f"{(input_temp - 273.15) * 9/5 + 32:.2f} °F")
            else:
                result.set(f"{input_temp:.2f} K")
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Input field
frame_input = ttk.Frame(root)
frame_input.pack(pady=10)

label_temp = ttk.Label(frame_input, text="Enter Temperature:")
label_temp.pack(side=tk.LEFT, padx=10)
entry_temp = ttk.Entry(frame_input)
entry_temp.pack(side=tk.LEFT)

# Unit conversion options
frame_units = ttk.Frame(root)
frame_units.pack(pady=10)

label_from_unit = ttk.Label(frame_units, text="From:")
label_from_unit.pack(side=tk.LEFT, padx=10)
combo_from_unit = ttk.Combobox(frame_units, values=("Celsius", "Fahrenheit", "Kelvin"))
combo_from_unit.pack(side=tk.LEFT)
combo_from_unit.set("Celsius")

label_to_unit = ttk.Label(frame_units, text="To:")
label_to_unit.pack(side=tk.LEFT, padx=10)
combo_to_unit = ttk.Combobox(frame_units, values=("Celsius", "Fahrenheit", "Kelvin"))
combo_to_unit.pack(side=tk.LEFT)
combo_to_unit.set("Fahrenheit")

# Convert button
btn_convert = ttk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack()

# Result label
result = tk.StringVar()
label_result = ttk.Label(root, textvariable=result)
label_result.pack(pady=10)

root.mainloop()
