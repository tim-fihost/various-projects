#caesar cipher
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2
print(art.logo)
def caeser(text,shift,direction):
    its_text = ""
    if shift > 30:
        if shift%2==0:
            shift=4
        else:
            shift = shift%26
    if direction == "decode":
        shift *=-1
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)    
            new_position = position + shift
            letter = alphabet[new_position]
            its_text += letter
        else:
            its_text += i
    print(f"The {direction}d text is {its_text}")
while True:
    direction = input("Type 'encode' to encrypt, type decode to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(message,shift,direction)
    will = input("Type any button if you want to continue, Type 'no' if you want to stop:\n").lower()
    if will == "no":
        break