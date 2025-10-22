# A Simple Dictionary

alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

print("\n")

# Accessing Values in a Dictionary

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print("\n")

# Adding New Key-Value Pairs

alien_0 = {"color": "green", "points": 5}

print(f"Original Dictionary: \n{alien_0}")

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(f"Update Dictionary: \n{alien_0}")

print("\n")

# Starting with an Empty Dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("\n")

# Modifying Values in a Dictionary

# Exanple 1
alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}.")

print("\n")

# Exanple 2
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original postion: {alien_0["x_position"]}")

#Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a Fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0['x_position']}")

print("\n")


# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

print("\n")