# *********************************************************************
# *                                                                   *
# *  Name:         Jack Vadasdi                                       *
# *  Class:        Computer Science II                                *
# *  Date:         9/30/2026                                          *
# *                                                                   *
# *********************************************************************
# *  Description:                                                     *
# *      toolkit that manipulates and sorts the                       *
# *      characters from a name                                       *
# *                                                                   *
# *********************************************************************
# *  Bugs:                                                            *
# *      Names have to be separated by single spaces.                 *
# *                                                                   *
# *********************************************************************

import random


def to_chars(text):
    """
    Description: Turns a string into an array of characters.
    Parameters:  text (str) - the text the user typed
    Returns:     list of single-character strings
    """
    chars = []
    for c in text:
        chars.append(c)
    return chars


def to_text(chars):
    """
    Description: Builds a string from an array of characters using
                 concatenation (+), since string methods are not allowed.
    Parameters:  chars (list) - array of characters
    Returns:     str - the characters joined together
    """
    text = ""
    for c in chars:
        text = text + c
    return text


def is_letter(c):
    """
    Description: Checks whether a single character is a letter A-Z or a-z.
    Parameters:  c (str) - one character
    Returns:     bool - True if c is a letter
    """
    return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z")


def is_vowel(c):
    """
    Description: Checks whether a single character is a vowel (any case).
    Parameters:  c (str) - one character
    Returns:     bool - True if c is a, e, i, o, or u
    """
    return c in "aeiouAEIOU"


def to_lower(chars):
    """
    Description: Converts every uppercase letter to lowercase. Returns a
                 NEW array; the original is not changed.
    Parameters:  chars (list) - array of characters
    Returns:     list - lowercase copy of the array
    """
    result = []
    for c in chars:
        if c >= "A" and c <= "Z":
            # In ASCII, a lowercase letter's code is 32 higher than the
            # matching uppercase letter ('A' = 65, 'a' = 97)
            result.append(chr(ord(c) + 32))
        else:
            result.append(c)
    return result


def to_upper(chars):
    """
    Description: Converts every lowercase letter to uppercase. Returns a
                 NEW array; the original is not changed.
    Parameters:  chars (list) - array of characters
    Returns:     list - uppercase copy of the array
    """
    result = []
    for c in chars:
        if c >= "a" and c <= "z":
            # Subtract 32 to move from the lowercase code to the uppercase code
            result.append(chr(ord(c) - 32))
        else:
            result.append(c)
    return result


def reverse_and_display(chars):
    """
    Description: Prints the characters in reverse order. The array itself
                 is not changed.
    Parameters:  chars (list) - array of characters
    Returns:     nothing (prints the result)
    """
    reversed_text = ""
    i = len(chars) - 1
    # Walk from the last index down to index 0
    while i >= 0:
        reversed_text = reversed_text + chars[i]
        i = i - 1
    print(reversed_text)


def count_vowels(chars):
    """
    Description: Counts all vowels (a, e, i, o, u) in any case.
    Parameters:  chars (list) - array of characters
    Returns:     int - total number of vowels
    """
    count = 0
    for c in chars:
        if is_vowel(c):
            count = count + 1
    return count


def count_one_vowel(chars, vowel):
    """
    Description: Counts how many times one particular vowel appears,
                 ignoring upper/lower case.
    Parameters:  chars (list) - array of characters
                 vowel (str) - the vowel to look for (one character)
    Returns:     int - number of times that vowel appears
    """
    count = 0
    target = to_lower([vowel])[0]       # make the vowel lowercase
    for c in to_lower(chars):           # compare against a lowercase copy
        if c == target:
            count = count + 1
    return count


def vowel_subtotals(chars):
    """
    Description: Counts each vowel separately.
    Parameters:  chars (list) - array of characters
    Returns:     list of 5 ints - counts for a, e, i, o, u (in that order)
    """
    vowels = "aeiou"
    counts = [0, 0, 0, 0, 0]
    for i in range(5):
        counts[i] = count_one_vowel(chars, vowels[i])
    return counts


def count_consonants(chars):
    """
    Description: Counts all consonants (letters that are not vowels).
    Parameters:  chars (list) - array of characters
    Returns:     int - total number of consonants
    """
    count = 0
    for c in chars:
        if is_letter(c) and not is_vowel(c):
            count = count + 1
    return count


def consonant_subtotals(chars):
    """
    Description: Counts how many times each consonant appears (Bonus).
    Parameters:  chars (list) - array of characters
    Returns:     list of 26 ints - index 0 is 'a', 1 is 'b', ... 25 is 'z'.
                 Vowel positions stay 0.
    """
    counts = [0] * 26
    for c in to_lower(chars):
        if is_letter(c) and not is_vowel(c):
            # ord(c) - ord('a') turns a letter into a position 0-25
            counts[ord(c) - ord("a")] += 1
    return counts


def first_name(chars):
    """
    Description: Returns the first name (everything before the first space).
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the first name
    """
    first = []
    for c in chars:
        if c == " ":
            break               # stop at the first space
        first.append(c)
    return first


def last_name(chars):
    """
    Description: Returns the last name (everything after the last space).
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the last name, or an empty list if
                 the name is only one word
    """
    if " " not in chars:
        return []
    last = []
    i = len(chars) - 1
    # Work backwards from the end until a space is reached,
    # inserting at position 0 so the letters stay in the right order
    while i >= 0 and chars[i] != " ":
        last.insert(0, chars[i])
        i = i - 1
    return last


def middle_names(chars):
    """
    Description: Returns the middle name(s): everything between the first
                 space and the last space.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the middle name(s), or an empty list
                 if there are fewer than two spaces
    """
    first_space = -1
    last_space = -1
    # Find the index of the first and last space
    for i in range(len(chars)):
        if chars[i] == " ":
            if first_space == -1:
                first_space = i
            last_space = i
    # Same index (or none found) means there is no middle name
    if first_space == last_space:
        return []
    middle = []
    for i in range(first_space + 1, last_space):
        middle.append(chars[i])
    return middle


def last_has_hyphen(chars):
    """
    Description: Checks whether the last name contains a hyphen.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     bool - True if the last name has a '-'
    """
    for c in last_name(chars):
        if c == "-":
            return True
    return False


def scramble(chars):
    """
    Description: Mixes up the letters. This MODIFIES the array that is
                 passed in instead of returning a new one.
    Parameters:  chars (list) - array of characters (changed in place)
    Returns:     nothing
    """
    for i in range(len(chars)):
        # Pick a random position and swap it with the current one
        j = random.randint(0, len(chars) - 1)
        temp = chars[i]
        chars[i] = chars[j]
        chars[j] = temp


# 11. Palindrome

def first_is_palindrome(chars):
    """
    Description: Checks whether the first name reads the same forwards
                 and backwards, ignoring upper/lower case.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     bool - True if the first name is a palindrome
    """
    first = to_lower(first_name(chars))
    # Only compare the first half to the mirrored second half
    for i in range(len(first) // 2):
        if first[i] != first[len(first) - 1 - i]:
            return False
    return True


# 12. Sorted characters (Bonus)

def sorted_chars(chars):
    """
    Description: Returns the full name as a sorted array of characters.
                 Spaces are removed and letters are made lowercase so the
                 order is alphabetical. Uses bubble sort on a copy.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - sorted characters
    """
    letters = []
    for c in to_lower(chars):
        if c != " ":
            letters.append(c)
    # Bubble sort: each pass pushes the largest remaining character to
    # the end, so the range of positions checked shrinks each pass
    for i in range(len(letters)):
        for j in range(len(letters) - 1 - i):
            if letters[j] > letters[j + 1]:
                temp = letters[j]
                letters[j] = letters[j + 1]
                letters[j + 1] = temp
    return letters


# 14. Initials


def initials(chars):
    """
    Description: Makes initials from the name, e.g. "mary jane watson"
                 becomes "M.J.W."
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the initials
    """
    result = []
    new_word = True              # True when the next letter starts a word
    for c in to_upper(chars):
        if c == " ":
            new_word = True
        elif new_word:
            result.append(c)
            result.append(".")
            new_word = False
    return result


# 15. Title check (Bonus)

def has_title(chars):
    """
    Description: Checks whether any word in the name is a title or
                 distinction such as Dr., Sir, Esq, or Ph.D (any case).
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     bool - True if a title is found
    """
    titles = ["dr", "dr.", "sir", "esq", "ph.d", "mr", "mr.", "mrs",
              "mrs.", "ms", "ms."]
    word = ""
    lowered = to_lower(chars)
    lowered.append(" ")          # extra space so the LAST word is checked too
    for c in lowered:
        if c == " ":
            if word in titles:
                return True
            word = ""            # start building the next word
        else:
            word = word + c
    return False



# 17. My own: Caesar cipher (Bonus)


def caesar(chars, shift):
    """
    Description: Encodes the text by moving each letter 'shift' places
                 along the alphabet, wrapping from z back to a. Output is
                 lowercase; non-letters are left alone.
    Parameters:  chars (list) - array of characters
                 shift (int) - number of places to move (negative decodes)
    Returns:     list - the encoded characters (a new array)
    """
    result = []
    for c in to_lower(chars):
        if c >= "a" and c <= "z":
            # 1. ord(c) - ord('a')   -> position in alphabet (0-25)
            # 2. + shift             -> move forward
            # 3. % 26                -> wrap around past 'z'
            # 4. + ord('a')          -> convert back to a letter code
            result.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(c)
    return result


# 13. Menu (Bonus)

def show_menu():
    """
    Description: Prints the list of menu options.
    Parameters:  none
    Returns:     nothing
    """
    print("\n--- MENU ---")
    print("1  Reverse")
    print("2  Vowels")
    print("3  Consonants")
    print("4  First name")
    print("5  Last name")
    print("6  Middle name(s)")
    print("7  Hyphen in last name?")
    print("8  Lowercase")
    print("9  Uppercase")
    print("10 Scramble")
    print("11 First name palindrome?")
    print("12 Sorted characters")
    print("14 Initials")
    print("15 Has title?")
    print("17 Caesar cipher")
    print("0  Quit")


def main():
    """
    Description: Asks for a name, then shows the menu and runs
                 the chosen function until the user enters 0.
    Parameters:  none
    Returns:     nothing
    """
    name = to_chars(input("Enter your name or a word: "))
    choice = ""
    while choice != "0":
        show_menu()
        choice = input("Choice: ")
        if choice == "1":
            reverse_and_display(name)
        elif choice == "2":
            print("Total vowels:", count_vowels(name))
            v = input("Which vowel do you want counted? ")
            if len(v) == 1 and is_vowel(v):
                print(v, "appears", count_one_vowel(name, v), "times")
            else:
                print("That is not a vowel.")
            print("Subtotals for a e i o u:", vowel_subtotals(name))
        elif choice == "3":
            print("Total consonants:", count_consonants(name))
            counts = consonant_subtotals(name)
            for i in range(26):
                if counts[i] > 0:
                    # chr(ord('a') + i) turns position i back into a letter
                    print(chr(ord("a") + i) + ":", counts[i])
        elif choice == "4":
            print(to_text(first_name(name)))
        elif choice == "5":
            print(to_text(last_name(name)))
        elif choice == "6":
            print(to_text(middle_names(name)))
        elif choice == "7":
            print(last_has_hyphen(name))
        elif choice == "8":
            print(to_text(to_lower(name)))
        elif choice == "9":
            print(to_text(to_upper(name)))
        elif choice == "10":
            scramble(name)       # changes the array itself
            print(to_text(name))
        elif choice == "11":
            print(first_is_palindrome(name))
        elif choice == "12":
            print(to_text(sorted_chars(name)))
        elif choice == "14":
            print(to_text(initials(name)))
        elif choice == "15":
            print(has_title(name))
        elif choice == "17":
            shift = int(input("Shift by: "))
            print(to_text(caesar(name, shift)))
        elif choice != "0":
            print("Invalid choice")
    print("Goodbye!")


main()