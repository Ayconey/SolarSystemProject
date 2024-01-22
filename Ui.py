import copy
import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from SolarSystemClasses import SolarSystem, SolarObject


class SolarSystemUI:
    def __init__(self, solar_system):
        # initial settings
        self.window = tk.Tk()
        self.window.title("Solar System")
        self.window.geometry("500x500")

        # Set the dark theme
        self.window.configure(bg="#383838")
        style = ttk.Style()
        style.theme_use("default")
        style.configure(".", background="#383838", foreground="white", fieldbackground="#383838")
        style.map('.', background=[('selected', 'black')], foreground=[('selected', 'white')])
        style.map('Treeview', background=[('selected', '#4A6984')], foreground=[('selected', 'white')])

        self.up_triangle = tk.PhotoImage(file="up_triangle.png")
        self.down_triangle = tk.PhotoImage(file="down_triangle.png")

        self.current_file = None

        # initialize solar system
        self.original_solar_system = solar_system
        self.solar_system = copy.deepcopy(solar_system)

        # Fields for the user input
        name_label = tk.Label(self.window, text="Name:", bg="#383838", fg="white")
        name_label.pack()
        self.name_entry = tk.Entry(self.window, width=30, bg="#383838", fg="white")
        self.name_entry.pack()

        mass_label = tk.Label(self.window, text="Mass:", bg="#383838", fg="white")
        mass_label.pack()
        self.mass_entry = tk.Entry(self.window, width=30, bg="#383838", fg="white")
        self.mass_entry.pack()

        distance_label = tk.Label(self.window, text="Distance to Sun:", bg="#383838", fg="white")
        distance_label.pack()
        self.distance_entry = tk.Entry(self.window, width=30, bg="#383838", fg="white")
        self.distance_entry.pack()

        period_label = tk.Label(self.window, text="Orbital Period:", bg="#383838", fg="white")
        period_label.pack()
        self.period_entry = tk.Entry(self.window, width=30, bg="#383838", fg="white")
        self.period_entry.pack()

        # Buttons
        add_button = tk.Button(self.window, text="Add", command=self.add_item, bg="#383838", fg="white")
        add_button.pack()

        # Create a frame for the buttons
        button_frame = tk.Frame(self.window, bg="#383838")
        button_frame.pack()

        # Buttons
        open_button = tk.Button(button_frame, text="Open", command=self.open_file, bg="#383838", fg="white")
        open_button.pack(side=tk.RIGHT, padx=1)

        save_as_button = tk.Button(button_frame, text="Save as", command=self.save_as, bg="#383838", fg="white")
        save_as_button.pack(side=tk.RIGHT, padx=1)

        save_button = tk.Button(button_frame, text="Save", command=self.save, bg="#383838", fg="white")
        save_button.pack(side=tk.RIGHT, padx=1)

        # Treeview for showing the solar system data in a table
        self.treeview = ttk.Treeview(self.window, columns=("#", "name", "mass", "distance_to_sun", "period"),
                                     show="headings", selectmode='extended')

        # Set the column headings and widths
        self.treeview.heading("#", text="#")
        self.treeview.column("#", width=30, anchor=tk.E)

        self.treeview.heading("name", text="Name", command=lambda: self.sort_column("name"))
        self.treeview.column("name", width=100)

        self.treeview.heading("mass", text="Mass", command=lambda: self.sort_column("mass"))
        self.treeview.column("mass", width=100, anchor=tk.E)

        self.treeview.heading("distance_to_sun", text="Distance to Sun",
                              command=lambda: self.sort_column("distance_to_sun"))
        self.treeview.column("distance_to_sun", width=100, anchor=tk.E)

        self.treeview.heading("period", text="Period", command=lambda: self.sort_column("period"))
        self.treeview.column("period", width=100, anchor=tk.E)

        # Initialize the sort order dictionary
        self.sort_order = {"#": True, "name": True, "mass": True, "distance_to_sun": True, "period": True}

        # Add data to the Treeview widget
        for i, obj in enumerate(self.solar_system.solar_objects, start=1):
            self.treeview.insert("", "end", values=(
                i, obj.name, "{:.2e}".format(obj.mass), "{:.2e}".format(obj.distance_to_sun),
                "{:.2e}".format(obj.period)),
                                 tags=('row',))

        # Change the color of the rows
        self.treeview.tag_configure('row', background='#383838', foreground='white')

        # Pack the Treeview widget into the window
        self.treeview.pack()

        delete_button = tk.Button(self.window, text="Delete", command=self.delete_item, bg="#383838", fg="white")
        delete_button.pack()

        # Start the main loop
        self.window.mainloop()

    def show(self):
        self.window.mainloop()

    # noinspection PyUnreachableCode
    def add_item(self):
        # get attributes from the entry fields
        name = self.name_entry.get()
        mass = self.mass_entry.get()
        distance_to_sun = self.distance_entry.get()
        period = self.period_entry.get()

        # error handling
        try:
            if name == "" or mass == "" or distance_to_sun == "" or period == "":
                raise ValueError("All fields must be filled. None of the fields can be empty.")

            # Check if name already exists in solar_objects
            for obj in self.solar_system.solar_objects:
                if obj.name == name:
                    raise ValueError("An item with this name already exists.")

            # handle scientific notation and negative values
            mass = float(mass)
            distance_to_sun = float(distance_to_sun)
            period = float(period)

            if mass < 0 or distance_to_sun < 0 or period < 0:
                raise ValueError("Mass, distance to sun, and period must be non-negative.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # create a new solar object
        new_solar_object = SolarObject(name, mass, distance_to_sun, period)

        # add the new solar object to the solar system
        self.solar_system.add(new_solar_object)

        # update the Treeview
        self.treeview.insert("", "end",
                             values=(len(self.solar_system.solar_objects), name, "{:.2e}".format(mass),
                                     "{:.2e}".format(distance_to_sun), "{:.2e}".format(period)),
                             tags=('row',))

        # clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.mass_entry.delete(0, tk.END)
        self.distance_entry.delete(0, tk.END)
        self.period_entry.delete(0, tk.END)

    def delete_item(self):
        selected_items = self.treeview.selection()
        for item in selected_items:
            # get the ordinal number of the object to remove
            ordinal_to_remove = int(
                self.treeview.item(item)['values'][0]) - 1  # subtract 1 because list indices start at 0

            # check if the ordinal number is valid
            if 0 <= ordinal_to_remove < len(self.solar_system.solar_objects):
                # remove the object from the solar system
                del self.solar_system.solar_objects[ordinal_to_remove]

        # clear the Treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        # refresh the Treeview
        for i, obj in enumerate(self.solar_system.solar_objects, start=1):
            self.treeview.insert("", "end", values=(
                i, obj.name, "{:.2e}".format(obj.mass), "{:.2e}".format(obj.distance_to_sun),
                "{:.2e}".format(obj.period)),
                                 tags=('row',))

    def save(self):
        if self.current_file is None:
            self.save_as()
        else:
            self.solar_system.save_to_file(self.current_file)

    def save_as(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV file", "*.csv")])
        if filename:
            self.solar_system.save_to_file(filename)

    def open_file(self):
        filename = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            try:
                # verify the input
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) != 4:
                            messagebox.showerror("Input Error", "Each row must have 4 columns.")
                            return
                        name, mass, distance_to_sun, period = row
                        try:
                            float(mass)
                            float(distance_to_sun)
                            float(period)
                        except ValueError:
                            messagebox.showerror("Input Error",
                                                 "The last three columns must be convertible to a float.")
                            return
            except UnicodeDecodeError:
                messagebox.showerror("Encoding Error", "File encoding must be UTF-8.")
                return

            self.solar_system.load_from_file(filename)

            # clear the Treeview
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # refresh the Treeview
            for i, obj in enumerate(self.solar_system.solar_objects, start=1):
                self.treeview.insert("", "end", values=(
                    i, obj.name, "{:.2e}".format(obj.mass), "{:.2e}".format(obj.distance_to_sun),
                    "{:.2e}".format(obj.period)), tags=('row',))

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            self.solar_system.solar_objects = [SolarObject(*row) for row in reader]

    def sort_column(self, column):
        # Sort the solar system
        self.solar_system.sort(column, self.sort_order[column])

        # Reverse the sort order for the next time
        self.sort_order[column] = not self.sort_order[column]

        # Clear the Treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        # Refresh the Treeview
        for i, obj in enumerate(self.solar_system.solar_objects, start=1):
            self.treeview.insert("", "end", values=(
                i, obj.name, "{:.2e}".format(obj.mass), "{:.2e}".format(obj.distance_to_sun),
                "{:.2e}".format(obj.period)),
                                 tags=('row',))

        # Set the column header image and text
        for col in self.treeview['columns']:
            if col == column:
                if self.sort_order[column]:
                    self.treeview.heading(col, image=self.up_triangle, text=col.capitalize())
                else:
                    self.treeview.heading(col, image=self.down_triangle, text=col.capitalize())
            else:
                self.treeview.heading(col, image='', text=col.capitalize() + ' ')
