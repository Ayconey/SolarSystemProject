import tkinter as tk
from SolarSystemClasses import SolarSystem, SolarObject


class SolarSystemUI:
    def __init__(self, solar_system):
        # initial settings
        self.window = tk.Tk()
        self.window.title("Solar System")
        self.window.geometry("500x500")

        # initialize solar system
        self.solar_system = solar_system

        # Fields for the user input
        name_label = tk.Label(self.window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.window, width=20)
        self.name_entry.pack()

        mass_label = tk.Label(self.window, text="Mass:")
        mass_label.pack()
        self.mass_entry = tk.Entry(self.window, width=20)
        self.mass_entry.pack()

        distance_label = tk.Label(self.window, text="Distance to Sun:")
        distance_label.pack()
        self.distance_entry = tk.Entry(self.window, width=20)
        self.distance_entry.pack()

        period_label = tk.Label(self.window, text="Orbital Period:")
        period_label.pack()
        self.period_entry = tk.Entry(self.window, width=20)
        self.period_entry.pack()

        # Buttons
        add_button = tk.Button(self.window, text="Add", command=self.add_item)
        add_button.pack()

        delete_button = tk.Button(self.window, text="Delete", command=self.delete_item)
        delete_button.pack()

        # Listbox for showing the solar system data
        self.listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        self.listbox.pack()

        # update the listbox with objects from solar system
        for solar_object in self.solar_system.solar_objects:
            self.listbox.insert(tk.END, str(solar_object))

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
        if name == "" or mass == "" or distance_to_sun == "" or period == "":
            raise ValueError("Please fill in all the fields")
            return

        if mass.isnumeric() == False or distance_to_sun.isnumeric() == False or period.isnumeric() == False:
            raise ValueError("Bad type of one or more fields, mass, distance and period must be numbers")
            return

        # create a new solar object
        new_solar_object = SolarObject(name, mass, distance_to_sun, period)

        # add the new solar object to the solar system
        self.solar_system.add(new_solar_object)

        # update the listbox
        self.listbox.insert(tk.END, str(new_solar_object))

        # clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.mass_entry.delete(0, tk.END)
        self.distance_entry.delete(0, tk.END)
        self.period_entry.delete(0, tk.END)

    def delete_item(self):
        selected_index = self.listbox.curselection()
        selected_item = self.listbox.get(selected_index) # item in string format
        self.solar_system.remove_item_from_string(selected_item)
        print(self.solar_system)

        if selected_index:
            self.listbox.delete(selected_index)
