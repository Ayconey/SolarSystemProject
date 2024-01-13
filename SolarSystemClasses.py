def cmp(a, b):
    x = a - b
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


class SolarObject:
    def __init__(self, name, mass, distance_to_sun, period):
        self.name = name
        self.mass = mass
        self.distance_to_sun = distance_to_sun
        self.period = period

    def __str__(self):
        return str(self.name) + " " + str(self.mass) + " " + str(self.distance_to_sun) + " " + str(self.period)

    # methods for comparisons
    def __lt__(self, other):
        if self.distance_to_sun != other.distance_to_sun:
            return self.distance_to_sun < other.distance_to_sun

        if self.mass != other.mass:
            return self.mass < other.mass

        return self.period < other.period

    def __le__(self, other):
        if self.distance_to_sun != other.distance_to_sun:
            return self.distance_to_sun <= other.distance_to_sun

        if self.mass != other.mass:
            return self.mass <= other.mass

        return self.period <= other.period

    def __eq__(self, other):
        if self.distance_to_sun != other.distance_to_sun:
            return self.distance_to_sun == other.distance_to_sun

        if self.mass != other.mass:
            return self.mass == other.mass

        return self.period == other.period

    def __ne__(self, other):
        if self.distance_to_sun != other.distance_to_sun:
            return self.distance_to_sun != other.distance_to_sun

        if self.mass != other.mass:
            return self.mass != other.mass

        return self.period != other.period

    def __gt__(self, other):
        if self.distance_to_sun != other.distance_to_sun:
            return self.distance_to_sun > other.distance_to_sun

        if self.mass != other.mass:
            return self.mass > other.mass

        return self.period > other.period

    def __ge__(self, other):
        if self.distance_to_sun != other.distance_to_sun:
            return self.distance_to_sun >= other.distance_to_sun

        if self.mass != other.mass:
            return self.mass >= other.mass

        return self.period >= other.period

    def compare_by(self, other, criterium):
        """
        Compares two objects based on the given criterium
        :param other:
        :param criterium:
        :return:
        """
        if criterium == "mass":
            return cmp(self.mass, other.mass)
        elif criterium == "distance_to_sun":
            return cmp(self.distance_to_sun, other.distance_to_sun)
        elif criterium == "period":
            return cmp(self.period, other.period)
        else:
            raise ValueError(
                "Invalid criterium: " + str(criterium) + "\nPossible criteria: mass, distance_to_sun, period")


class SolarSystem:
    """
    Solar system class
    """

    def __init__(self, solar_objects):
        """
        :param solar_objects: list of solar objects
        """
        self.solar_objects = solar_objects
        self.update_file()

    def __len__(self):
        return len(self.solar_objects)


    def __sub__(self, solar_object):
        self.solar_objects.remove(solar_object)
        self.update_file()
        print(self.solar_objects)

    def __str__(self):
        # read the solar objects from the file
        solar_system_file = open("solar_system.txt", "r")
        objects = solar_system_file.readlines()
        solar_system_file.close()

        # replace \n with empty string
        for i in range(0, len(objects)):
            objects[i] = objects[i].replace("\n", "")

        return str(objects)

    def add(self, solar_object):
        self.solar_objects.append(solar_object)
        self.update_file()

    def remove_item_from_string(self, item):
        selected_item = item.split(" ")

        for o in self.solar_objects:
            if o.name == selected_item[0] and str(o.mass) == selected_item[1] and str(o.distance_to_sun) == selected_item[2] and str(o.period) == selected_item[3]:
                self.solar_objects.remove(o)
                break
        self.update_file()

    def sort(self):
        # do zrobienia kubełkowo
        self.solar_objects.sort()
        self.update_file()

    def sort_by(self, criteria):
        # do zrobienia kubełkowo
        pass

    def update_file(self):
        # create a file to store the solar system
        solar_system_file = open("solar_system.txt", "w")
        # Add solar objects to the solar system file
        for solar_object in self.solar_objects:
            solar_system_file.write(str(solar_object) + "\n")
        solar_system_file.close()