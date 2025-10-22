# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    "new york": {
        "contry": "america",
        "approximate_population": "8,478,072",
        "key_fact": "It was the first capital of the United States, serving from 1785 to 1791, and the first pizzeria in the U.S. opened there in 1905."
    },
    "paris": {
        "contry": "france",
        "approximate_population": "2,048,472",
        "key_fact": "There are no stop signs in the city, as it operates on a right-of-way rule for traffic. The Eiffel Tower was originally intended to be temporary, the Louvre is the world's largest art museum, and the city has five replicas of the Statue of Liberty."
    },
    "rome": {
        "contry": "italy",
        "approximate_population": "4,223,885",
        "key_fact": "Rome is a city of fountains with over 1500, has more churches than any other city, and has the world's smallest country, Vatican City, entirely within its borders."
    }
}

for city, facts in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tApproximate Population: {facts["approximate_population"]}")
    print(f"\tKey Fact: {facts["key_fact"]}")
