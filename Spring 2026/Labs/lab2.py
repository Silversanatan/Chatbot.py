def pair_frequencies(word_list):
    counts = {}
    for word in word_list:
        for i in range(len(word) - 1):
            pair = word[i : i + 2]
            if pair in counts:
                counts[pair] += 1
            else:
                counts[pair] = 1
    for pair in counts:
        print(str(pair),":",str(counts[pair]))

def main():
    pair_frequencies(["banana","bends","i","mend","sandy"])
main()