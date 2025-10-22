#KH 2nd period caesar code

print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")


def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if mode == encrypt 