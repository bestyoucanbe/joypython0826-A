planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Neptune", "Uranus"])
planet_list.insert(2, "Earth")
planet_list.insert(3, "Venus")
planet_list.append("pluto")

# using slice to obtain the rocky planets
rocky_planets = planet_list[slice(0, 3)]

# using delete to remove the last planet
del planet_list[8]

print("planet list-->", planet_list)
print("rocky planets-->", rocky_planets)
