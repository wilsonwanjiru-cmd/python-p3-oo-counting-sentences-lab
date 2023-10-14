#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print('The value must be a string.')
    
    value = property(get_value, set_value)

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        sentence = self._value
        character = ['.','!','?']
        for i in sentence:
            if i in character:
                sentence = sentence.replace(i,'-')
        result = re.split('-',sentence)
        new = [word for word in result if word != '']
        length = len(new)
       
        return length


string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())

