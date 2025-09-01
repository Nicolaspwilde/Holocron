cities = {
    "Paris": {
        "country": "France",
        "population_millions": 11,
        "famous_for": "Eiffel Tower"
    },
    "Tokyo": {
        "country": "Japan",
        "population_millions": 37,
        "famous_for": "Technology and Sushi"
    },
    "New York": {
        "country": "USA",
        "population_millions": 19,
        "famous_for": "Statue of Liberty"
    }
}
city_input = input("enter the city : ").title()
if city_input in cities:
    print("city exist in our list :) ")
    print(f"{city_input} is in {cities[city_input]['country']} ")
    print(f"{city_input} has population of {cities[city_input]['population_millions']}")
    print(f"It is famous for {cities[city_input]['famous_for']}")
else :
    print("the city is not in our list")
    for city in cities :
        print(city)