# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word
        self.word_sorted = sorted(word)

    def match(self, word_list):
        matching_words = []        
        for word in word_list:
            if self.word != word and sorted(word) == self.word_sorted:
                matching_words.append(word)
        return matching_words
        
