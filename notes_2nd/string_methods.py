# KH 2nd strings method notes

# a method is a prebuilt code to complete a task that is specific data type
# a string can bee an empty space, number, and any letters.

name = input("what is your name:    ").strip().title()
#.lower() => makes it all lower case
#.upper() => makes it all upper case
#.capitalize() => captializes the first letter
#.title() => capitalizes the first letter of every word


print("Hello {}, it is nice to meet you!".format
(name))

print(f"Hello {name}, it is nice to meet you!")

#age = input("Bro how old are you")
#print(age.isdigit())
#print("Really? " + age + " is old")

sentence = "The quick brown fox jumps over the lazy dog!"

word = "over"
start = (sentence.find(word))
#length = len()

#print(sentence,replace(word, "yellow"))

