alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    final_text=""
    for letter in text:
        index=alphabet.index(letter)
        if direction == "encode":
            new_index=index+shift
            final_text+=alphabet[new_index]
        else:
            new_index=index-shift
            final_text+=alphabet[new_index]
        
    print(final_text)
    
caesar(direction, text, shift)

# def decrypt(cipher_text, shift):
#     text=""
#     for letter in cipher_text:
#         index=alphabet.index(letter)
#         new_index=index-shift
#         text+=alphabet[new_index]
#         
#     print(text)
#     
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid command")

        
