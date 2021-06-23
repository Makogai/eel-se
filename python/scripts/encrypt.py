from typing import Text

class AlphaShift:
    print("Heree")
    def __init__(self,text):
        self.text = text
    
    def encrypt(self):
        new_message = ''
        for letter in self.text:
            letter_number = ord(letter)
            new_letter_number = letter_number + 1
            new_letter = chr(new_letter_number)
            new_message = new_message + new_letter
        return new_message

    def decrypt(self):
        new_message = ''
        for letter in self.text:
            letter_number = ord(letter)
            new_letter_number = letter_number - 1
            new_letter = chr(new_letter_number)
            new_message = new_message + new_letter
        return new_message

class AlphaMix:
    def __init__(self,text, key):
        self.text = text
        self.secret_key = int(key)
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def encrypt(self):
        new_message = ""
        for character in self.text:
            if character.isalpha():
                character = character.lower()
                character_index = self.alphabet.index(character)
                new_index = (character_index + self.secret_key) % 26
                enc_char = self.alphabet[new_index].upper()
            else:
                enc_char = character
            new_message += enc_char
        return new_message
    
    def decrypt(self):
        decoded = ""
        for character in self.text:
            if character.isalpha():
                character = character.lower()
                character_index = self.alphabet.index(character)
                new_index = (character_index - self.secret_key) % 26
                dec_char = self.alphabet[new_index]
            else:
                dec_char = character
            decoded += dec_char
        return decoded


def encrypt(text):
    new_message = ''
    for letter in text:
        letter_number = ord(letter)
        new_letter_number = letter_number + 1
        new_letter = chr(new_letter_number)
        new_message = new_message + new_letter
    return new_message
