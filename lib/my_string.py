class MyString:
    def __init__(self):
        self.value = ''

    def is_sentence(self):
        if not isinstance(self.value, str):
            print("The value must be a string.")
            return False
        return self.value.endswith('.')

    def is_question(self):
        if not isinstance(self.value, str):
            print("The value must be a string.")
            return False
        return self.value.endswith('?')

    def is_exclamation(self):
        if not isinstance(self.value, str):
            print("The value must be a string.")
            return False
        return self.value.endswith('!')

    def count_sentences(self):
        if not isinstance(self.value, str):
            print("The value must be a string.")
            return 0

        sentences = self.value.split('.') + self.value.split('?') + self.value.split('!')
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)
