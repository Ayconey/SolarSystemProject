from SolarSystemClasses import SolarSystem, SolarObject


# example objects
Earth = SolarObject("Earth", 1.989e30, 6, 1)
Mars = SolarObject("Mars", 6.417e23, 3.389, 1)
Jupiter = SolarObject("Jupiter", 1.898e27, 7.784, 1)
Saturn = SolarObject("Saturn", 5.682e26, 14, 1)
Uranus = SolarObject("Uranus", 8.685e25, 28, 1)
Neptune = SolarObject("Neptune", 1.024e26, 84, 1)

solar_system = SolarSystem([Earth, Mars, Jupiter, Saturn, Uranus, Neptune])
print(solar_system)
solar_system.sort()
print(solar_system)
solar_system += Earth