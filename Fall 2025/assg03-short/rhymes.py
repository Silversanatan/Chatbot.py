"""
    File: rhymes.py
    Author: Rajat Tawari
    Course: CSC 120, Fall 2025
    Purpose: This program reads a file containing word pronunciations, 
        prompts the user for a target word, and finds all words in the
        file that rhyme with the target word. The rhyming words are then
        printed to the console in alphabetical order.
"""

def get_rhyme_components(pronunciation):
    """Identifies the rhyming part of a word's pronunciation based on
    the location of the primary stress. The rhyming part starts from the
    first stressed vowel.
    Parameters: pronunciation is a list of strings representing the
        phonemes of a word.
    Returns: A tuple containing two elements:
        1. A list of phonemes that form the rhyming component.
        2. The single phoneme immediately preceding the rhyming component.
        If no primary stress ('1') is found, returns (None, None).
    """
    stress_i = -1
    i = 0
    # Loop through the phonemes to find the primary stress, marked by '1'.
    while i < len(pronunciation) and stress_i == -1:
        phoneme = pronunciation[i]
        if '1' in phoneme:
            stress_i = i
        i += 1
    # If no primary stress was found, the word cannot be used for rhyming.
    if stress_i == -1:
        return (None, None)
    # The rhyming part consists of all phonemes from the stress to the end.
    rhyme = pronunciation[stress_i:]
    earlier_phoneme = None
    # Get the phoneme immediately before the stressed vowel, if one exists.
    if stress_i > 0:
        earlier_phoneme = pronunciation[stress_i - 1]
    return (rhyme, earlier_phoneme)

def build_pronunciation_dict(pfile_name):
    """Reads a pronunciation file and builds a dictionary mapping each
    word to a list of its possible pronunciations.
    Parameters: pfile_name is a string with the name of the file to read.
    Returns: A dictionary where keys are words (strings) and values are
        lists of pronunciations.
    """
    pronunciation_dict = {}
    pfile = open(pfile_name, 'r')
    # Read the file line by line to populate the dictionary.
    for line in pfile:
        parts = line.split()
        word = parts[0]
        phonemes = parts[1:]
        # This handles words with multiple valid pronunciations.
        if word in pronunciation_dict:
            pronunciation_dict[word].append(phonemes)
        else:
            pronunciation_dict[word] = [phonemes]
    pfile.close()
    return pronunciation_dict

def find_rhyming_words(target_word, pronunciation_dict):
    """Finds all words in the pronunciation dictionary that rhyme with the
    target word.
    Parameters: 
        target_word: The string word to find rhymes for.
        pronunciation_dict: The dictionary of words and pronunciations.
    Returns: A list of strings, where each string is a word that rhymes
        with the target_word.
    """
    target_word_upper = target_word.upper()
    target_pronunciations = pronunciation_dict[target_word_upper]
    rhyming_words = []
    # Iterate through all possible pronunciations of the target word.
    for target_pron in target_pronunciations:
        (target_rhyme, target_pre) = get_rhyme_components(target_pron)
        # Only proceed if the target word has a valid rhyming component.
        if target_rhyme is not None:
            # Compare with every pronunciation of all words in the dictionary.
            for word, candidate_prons in pronunciation_dict.items():
                # Check each possible pronunciation for the candidate word.
                for candidate_pron in candidate_prons:
                    (cand_rhyme,cand_pre)=get_rhyme_components(candidate_pron)
                    if cand_rhyme is not None:
                        if target_rhyme==cand_rhyme and target_pre!=cand_pre:
                            rhyming_words.append(word)
    return rhyming_words

def main():
    pfile_name = input()
    pronunciation_dict = build_pronunciation_dict(pfile_name)
    target_word = input()
    rhyming_words = find_rhyming_words(target_word, pronunciation_dict)
    # Sort the final list of rhyming words alphabetically before printing.
    rhyming_words.sort()
    for word in rhyming_words:
        print(word)
main()