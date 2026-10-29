# This program changes meters to other units.

meters = float(input("Enter a length in meters: "))

kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

print("Kilometers:", kilometers)
print("Hectometers:", hectometers)
print("Decameters:", decameters)
print("Meters:", meters)
print("Decimeters:", decimeters)
print("Centimeters:", centimeters)
print("Millimeters:", millimeters)