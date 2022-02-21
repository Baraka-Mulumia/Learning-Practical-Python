# nested dictionaries and values
cities = {
    "France": "paris",
    "Germany": "Berlin",
    "Kenya": ["Nairobi", "Mombasa", "Juja"]
}

users = {
    "baraka": {
        "name": "Baraka Mulumia",
        "age": 23,
        "likes": ["coding", "dancing", "movies"]
    },
    "jane": {
        "name": "Jane Draco",
        "age": 21,
        "likes": ["tik tok", "skiing", "movies"]
    }
}

print(users["baraka"]["name"])
print(users["jane"]["likes"][0])

travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille"],
        "total_visits": 14
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3
    },

]

print(travel_log)

# exercise 9.2


def add_new_log(country, cities, total_visits):
    travel_log.append({
        "country": country,
        "cities": cities,
        "total_visits": total_visits
    })


add_new_log("Russia", ["Moscow",  "St Peter'sbug"], 4)
print(travel_log)
