# read animals.txt
# and write animals_new.txt
animals = []
file_animals = open("animals.txt", "r")
animals = file_animals.read().split("\n")
file_animals.close()
file_animals_new = open("animals_new.txt", "w")
for i in animals:
    file_animals_new.write(i + " ")
file_animals_new.close()