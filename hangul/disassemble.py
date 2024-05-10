from .constants import (
    DISASSEMBLED_CONSONANTS_BY_CONSONANT,
    DISASSEMBLED_VOWELS_BY_VOWEL,
)
from .disassemble_complete_hangul_character import disassemble_complete_hangul_character


def disassemble_hangul_to_groups(string):
    result = []
    for letter in string:
        disassembled_complete = disassemble_complete_hangul_character(letter)

        if disassembled_complete is not None:
            # Append all parts of the disassembled character
            result.append(
                [
                    *list(disassembled_complete["first"]),
                    *list(disassembled_complete["middle"]),
                    *list(disassembled_complete["last"]),
                ]
            )
            continue

        # Check if the letter is a disassembled consonant
        if letter in DISASSEMBLED_CONSONANTS_BY_CONSONANT:
            disassembled_consonant = DISASSEMBLED_CONSONANTS_BY_CONSONANT[letter]
            result.append(list(disassembled_consonant))
            continue

        # Check if the letter is a disassembled vowel
        if letter in DISASSEMBLED_VOWELS_BY_VOWEL:
            disassembled_vowel = DISASSEMBLED_VOWELS_BY_VOWEL[letter]
            result.append(list(disassembled_vowel))
            continue

        # If none of the above, treat the letter as a single-item list
        result.append([letter])

    return result


def disassemble_hangul(string):
    groups = disassemble_hangul_to_groups(string)
    return "".join("".join(group) for group in groups)
