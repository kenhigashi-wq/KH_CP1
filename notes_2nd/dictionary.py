#KH 2nd dictionaries


person = {
    #key: value,
    "name": "Katie",
    "age": 37,
    "job": "jobless",
    "sibs": ["qwerty", "idi", "hi"]
}

print(person["age"])# Only one of the vars in the dictionary
print(person.keys())# calling entire dictionary
for key in person.keys():
    if key == "sibs":
        for sib in person[key]:
            print(f"{person['name']} has a sibling named {sib}")
    else:
        print(f"{key} is {person[key]}")
print(person.value)
person["age"] += 1
print(person["age"])
person["birthday"] = "June 8"
print(person.values())