"""
    File: rhymes.py
    Author: Rajat Tawari
    Course: CSC 120, Spring 2025
    Purpose: This script analyzes phonetic data to identify "perfect rhymes" 
        for a user-specified word. It processes a dictionary of sounds and 
        filters for words that share the same stressed ending but differ 
        in the sound immediately preceding that stress.
"""

def build_pronunciation_dict(pfile_name):
    """
    Loads phonetic data from a text file into a Python dictionary.
    
    Parameters:
        pfile_name: The name/path of the text file to be opened.
    Returns:
        A dictionary structured as {WORD: [[SOUNDS_1], [SOUNDS_2]]}.
    """
    pronunciation_dict = {}
    pfile = open(pfile_name, 'r')
    
    # Process the file line by line to extract word and phoneme data
    for line in pfile:
        parts = line.split()
        word = parts[0]
        phonemes = parts[1:]
        
        # Add new pronunciation to existing list or create a new entry
        if word in pronunciation_dict:
            pronunciation_dict[word].append(phonemes)
        else:
            pronunciation_dict[word] = [phonemes]
            
    pfile.close()
    return pronunciation_dict

def get_rhyme_components(pronunciation):
    """
    Extracts the phonetic parts necessary to determine a rhyme.
    
    Parameters: 
        pronunciation: A list of strings (phonemes) for a single word.
    Returns: 
        A tuple (rhyme_part, lead_sound). rhyme_part is the list of 
        phonemes from the primary stress to the end. lead_sound is the 
        single phoneme before the stress.
    """
    stress_i = -1
    i = 0
    # Search the list of sounds for the one containing the primary stress ('1')
    while i < len(pronunciation) and stress_i == -1:
        phoneme = pronunciation[i]
        if '1' in phoneme:
            stress_i = i
        i += 1
        
    # Validation check: ensure the word actually has a stressed vowel
    if stress_i == -1:
        return (None, None)
        
    # Slice the phoneme list to get the "tail" of the word
    rhyme = pronunciation[stress_i:]
    earlier_phoneme = None
    
    if stress_i > 0:
        earlier_phoneme = pronunciation[stress_i - 1]
        
    return (rhyme, earlier_phoneme)

def find_rhyming_words(target_word, pronunciation_dict):
    """
    Scans the entire dictionary to find every word that satisfies 
    perfect rhyme criteria with the input word.
    
    Parameters:
        target_word: The string to match against.
        pronunciation_dict: Dictionary mapping words to lists of phonemes.
    Returns:
        A list of all discovered rhyming words.
    """
    target_word_upper = target_word.upper()
    target_pronunciations = pronunciation_dict[target_word_upper]
    rhyming_words = []
    
    # Check every possible way the target word can be pronounced
    for target_pron in target_pronunciations:
        (target_rhyme, target_pre) = get_rhyme_components(target_pron)
        
        if target_rhyme is not None:
            # Look through every entry in our phonetic database
            for word, candidate_prons in pronunciation_dict.items():
                # Test each pronunciation of the candidate word
                for candidate_pron in candidate_prons:
                    (cand_rhyme, cand_pre) = \
                        get_rhyme_components(candidate_pron)
                    
                    if cand_rhyme is not None:
                        if target_rhyme == cand_rhyme and \
                            target_pre != cand_pre:
                            rhyming_words.append(word)
    return rhyming_words

def main():
    pfile_name = input()
    pronunciation_dict = build_pronunciation_dict(pfile_name)
    target_word = input()
    
    rhyming_words = find_rhyming_words(target_word, pronunciation_dict)
    
    rhyming_words.sort()
    for word in rhyming_words:
        print(word)

main()