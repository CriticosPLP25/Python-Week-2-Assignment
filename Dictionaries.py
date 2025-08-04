#Dictionaries in Python
capital_city ={"Kenya": "Nairobi", "Uganda": "Kampala", "Tanzania": "Dodoma", "Rwanda": "Kigali", "Burundi": "Gitega"}
print(capital_city["Kenya"]) 
print(capital_city)
 
 #Dictionaries with Intergers
price = {"Apple": 100, "Banana": 50, "Orange": 75, "Mango": 120}
print(price)
print(price["Banana"])
# Adding a new key-value pair
price["Grapes"] = 90
print(price)
# Removing a key-value pair
del price["Orange"]
print(price)
del(capital_city["Burundi"])
print(capital_city)
# Checking if a key exists
if "Kenya" in capital_city:
    print("Kenya is in the dictionary.")
else:
    print("Kenya is not in the dictionary.")
# Iterating through keys and values
for country, city in capital_city.items():
    print(f"The capital of {country} is {city}.")
# Merging two dictionaries
additional_countries = {"South Sudan": "Juba", "Ethiopia": "Addis Ababa"}
capital_city.update(additional_countries)
print(capital_city)
# Nested dictionaries
countries_info = {
    "Kenya": {"capital": "Nairobi", "population": 53771296},
    "Uganda": {"capital": "Kampala", "population": 45741007},
    "Tanzania": {"capital": "Dodoma", "population": 59734218},
    "Rwanda": {"capital": "Kigali", "population": 12952218},
    "Burundi": {"capital": "Gitega", "population": 12114505}
}
print(countries_info["Kenya"]["capital"])
print(countries_info["Uganda"]["population"])
# Accessing all keys and values
print("Countries:", list(countries_info.keys()))
print("Capitals:", list(countries_info.values()))
# Checking the length of a dictionary
print("Number of countries:", len(countries_info))
print("Numbwer of Capital Cities:", len(capital_city))








