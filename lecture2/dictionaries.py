ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1

print(ages)

for key in ages:
    print(f"{key} is {ages[key]} years old.")
