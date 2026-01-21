info = {
    "name": "Sumukh",
    "age": 20,
    "marks": {
        "math": 85,
        "science": 90,
        "english": 78,
    }
}

print(info)

info.keys()  # Returns a view object of keys

info.values()  # Returns a view object of values

info.items()  # Returns a view object of key-value pairs

info.get("name")  # Returns the value for the specified key

info.update({"age": 21})  # Updates the value for the specified key