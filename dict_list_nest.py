# nesting

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        "rating": "excellent",
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 6,
        "rating": "excellent",
    },
}

# turn dictionaries into lists
# we have a list which contains 2 items, and each is a dictionary
# each dictionary has 3 key:value pairs
# they all contain different types of data
# 1st a string, 2nd a list and 3rd a number

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        "rating": "excellent",
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 6,
        "rating": "excellent",
    },
]
print(travel_log)

# total dictionaries for France and Germany
