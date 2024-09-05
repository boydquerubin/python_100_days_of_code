capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# for country in travel_log:
    # print(country)
    # print(travel_log[country])
    # print(travel_log[country][1])

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 8
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 2
    }
}

print(travel_log["Germany"]["cities_visited"][2])