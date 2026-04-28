import sys

class Word:
    def __init__(self, word):
        self._word = word
        self._count = 1

    def word(self):
        return self._word

    def count(self):
        return self._count

    def incr(self):
        self._count += 1

    def __lt__(self, other):
        if self.count() != other.count():
            return self.count() > other.count()
        else:
            return self.word() < other.word()

    def __str__(self):
        return f"{self._word} : {self._count}"

    def __repr__(self):
        return self.__str__()

def merge(L1, L2):
    result = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    result.extend(L1[i:])
    result.extend(L2[j:])
    return result

def msort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = msort(L[:mid])
    right = msort(L[mid:])
    return merge(left, right)

def main():
    sys.setrecursionlimit(4000)
    lines = sys.stdin.readlines()
    N = len(lines)
    word_dict = {}
    for line in lines:
        words = line.strip().split()
        for w in words:
            w = w.lower()
            if w in word_dict:
                word_dict[w].incr()
            else:
                word_dict[w] = Word(w)
    word_list = list(word_dict.values())
    sorted_list = msort(word_list)
    print(f"File: {N}:")
    for i in range(min(10, len(sorted_list))):
        print(sorted_list[i])

main()