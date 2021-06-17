from typing import Text

class AlphaShift:
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