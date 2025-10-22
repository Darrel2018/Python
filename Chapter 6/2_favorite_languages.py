# A Dictionary of Similar Objects

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

print("\n")

# Using get() to Access Values

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

print("\n")

