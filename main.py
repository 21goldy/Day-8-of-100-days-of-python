import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"\nHere's the {cipher_direction}d result: {end_text}")
  
print(art.logo)

yes = True
while yes:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
  if direction == 'encode' or direction == 'decode':
    input_message = input("\nType your message: ").lower()
    text = input_message.replace(" ", "")
    shift = int(input("\nType the shift number: "))
    
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    play_again = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").lower()
    
    if play_again == "no":
      yes = False
      print("\nGood bye!😊")
  
  else:
    yes = False
    print('\nInvalide Output! Program Terminated.')
