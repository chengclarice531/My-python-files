fav_food = {}
food1 = input(f"What's your favorite food? ").capitalize()
food2 = input(f"What's your second favorite food? ").capitalize()
food3 = input(f"What's your third favorite food? ").capitalize()
food4 = input(f"What's your fourth favorite food? ").capitalize()
fav_food[1] = food1
fav_food[2] = food2
fav_food[3] = food3
fav_food[4] = food4
print("Here are your favorite foods:")
print(fav_food)
remove = int(input("Remove one of the food items by entering its number (1-4): "))
del fav_food[remove]
print(sorted(fav_food.values()))
