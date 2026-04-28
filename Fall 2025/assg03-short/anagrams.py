class Word:
    """Implement your class here"""
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return self._word.lower()

    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return sorted(self._word.lower()) == sorted(other._word.lower())