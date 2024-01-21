from SolarSystemClasses import SolarSystem, SolarObject
from Ui import SolarSystemUI

# example objects
Mercury = SolarObject("Mercury", 3.3011e23, 0.39, 0.24)
Venus = SolarObject("Venus", 4.8675e24, 0.723, 0.62)
Earth = SolarObject("Earth", 5.972e24, 1, 1)
Mars = SolarObject("Mars", 6.417e23, 1.524, 1.88)
Jupiter = SolarObject("Jupiter", 1.898e27, 5.203, 11.86)
Saturn = SolarObject("Saturn", 5.683e26, 9.582, 29.46)
Uranus = SolarObject("Uranus", 8.681e25, 19.18, 84.02)
Neptune = SolarObject("Neptune", 1.024e26, 30.07, 164.8)

example_objects = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

solar_system = SolarSystem(example_objects)

UI = SolarSystemUI(solar_system)
UI.show()
