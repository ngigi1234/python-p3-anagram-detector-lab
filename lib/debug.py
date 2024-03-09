class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        return [candidate for candidate in candidates if self.is_anagram(candidate)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        if candidate_lower == self.word:
            return False  
        return sorted(candidate_lower) == sorted(self.word)
