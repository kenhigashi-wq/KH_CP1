#KH 2nd period caesar code
#test
print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")

# make function for the cipher
def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')# checks if upper case
            shifted_code = (ord(char) - start + shift) % 26 + start # does the thing 
            result += chr(shifted_code)
        else:
            result += char
    return result
def decode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')# checks if upper case
            shifted_code = (ord(char) - start - shift) % 26 + start # also smae thing
            result += chr(shifted_code)
        else:
            result += char
    return result
# set message var
message = input("Enter your message: ")
#set the key var
key = int(input("Enter shift key: "))
#set the opertion var
op = input("Choose operation (1 for encode, 2 for decode): ")
    
# make the option thing
if op == "1":
    encrypted_message = encode(message, key)
    print(f"Encrypted message: {encrypted_message}")
elif op == "2":# do it for decode too
    decrypted_message = decode(message, key)
    print(f"decrypted message: {decrypted_message}")
else:# make else statement
    print("Invalid: Try again")