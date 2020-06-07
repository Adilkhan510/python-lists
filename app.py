students = ["adil", "pouyesh", "linh"]

print(students[1])
print(students[2])

FOODS = ["mac n cheese", "lasagna", "ramen"]


# for food in FOODS:
#     print(food + " is a good food")


for x in range(1,3):
    print(FOODS[x])


home_town = {
    "state" : "CA",
    "population": "1hunnnid",
    "city": "Fremont"
}

print("I was born in " + home_town['city']+"","" + home_town['state']+ " , and " + home_town[
'population'])


print(f"I was born in {home_town['city'], {home_town['state']}, with a population of {home_town['population']}}")


