def primary_stress_position(phoneme_list):
    for i, phoneme in enumerate(phoneme_list):
        if phoneme.endswith('1'):
            return i
    return None