sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694}, "Tom":{"N":4832, "S":6786, "E":4737, "W":3612}, "Anne":{"N":5239, "S":4802, "E":5820, "W":1859}, "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}
name = input("Enter a name (John, Tom, Anne, Fiona): ").capitalize()
region = input("Enter a region (N, S, E, W): ").upper()
print(sales[name][region])
name_change = input("Enter a name (John, Tom, Anne, Fiona): ").capiJtalize()
region_change = input("Enter a region (N, S, E, W): ").upper()
NewValue = int(input(f"Enter {name_change}'s updated sales figures for region {region_change}: "))
sales[name_change][region_change] = NewValue
print(sales[name_change])