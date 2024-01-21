import csv

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

    def __init__(self, solar_objects=None):
        """
        :param solar_objects: list of solar objects
        """
        self.solar_objects = solar_objects

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in self.solar_objects:
                writer.writerow([obj.name, obj.mass, obj.distance_to_sun, obj.period])

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            self.solar_objects = [SolarObject(*row) for row in reader]

    def __len__(self):
        return len(self.solar_objects)

    def __sub__(self, solar_object):
        self.solar_objects.remove(solar_object)
        print(self.solar_objects)

    def __str__(self):
        return str(self.solar_objects)

    def add(self, solar_object):
        self.solar_objects.append(solar_object)

    def remove_item_from_string(self, item):
        selected_item = item.split(" ")

        for o in self.solar_objects:
            if o.name == selected_item[0] and str(o.mass) == selected_item[1] and str(o.distance_to_sun) == \
                    selected_item[2] and str(o.period) == selected_item[3]:
                self.solar_objects.remove(o)
                break

    def sort(self, criteria, reversed=False):
        # Define a function to get the key for sorting based on the specified criteria
        def get_key(obj):
            if criteria == 'mass':
                return obj.mass
            elif criteria == 'distance_to_sun':
                return obj.distance_to_sun
            elif criteria == 'period':
                return obj.period
            else:
                # If an invalid criteria is provided, default to sorting by name
                return obj.name

        # Create buckets to store SolarObjects
        buckets = {}

        # Distribute SolarObjects into buckets based on the chosen criteria
        for solar_object in self.solar_objects:
            key = get_key(solar_object)
            if key in buckets:
                buckets[key].append(solar_object)
            else:
                buckets[key] = [solar_object]

        # Sort each bucket individually (using any sorting algorithm, e.g., built-in sorted function)
        for key in buckets:
            buckets[key] = sorted(buckets[key], key=lambda x: x.name, reverse=reversed)

        # Concatenate sorted buckets to get the final sorted list
        sorted_solar_objects = []
        for key in sorted(buckets.keys(), reverse=reversed):
            sorted_solar_objects.extend(buckets[key])

        # Update the SolarSystem's solar_objects attribute with the sorted list
        self.solar_objects = sorted_solar_objects

    def remove(self, name):
        for solar_object in self.solar_objects:
            if solar_object.name == name:
                self.solar_objects.remove(solar_object)
                break
