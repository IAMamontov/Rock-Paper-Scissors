# create the planets.txt
file_planets = open("planets.txt", "w", encoding="utf-8")
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
for i in planets:
    file_planets.write(i + "\n")
file_planets.close()