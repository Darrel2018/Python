# 8-14. Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def make_car(manufacturer, model_name, **additional_car_information):
    additional_car_information["manufacturer"] = manufacturer
    additional_car_information["model_name"] = model_name

    return additional_car_information

print(make_car("subaru", "outback", color="blue",
                                    tow_package=True))

