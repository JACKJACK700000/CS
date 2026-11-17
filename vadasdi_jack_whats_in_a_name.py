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
# *  Log:                                                             *
# *      V1: First submitted version, no line doc                     *
# *      V1.1: Line Documentation added                               *
# *                                                                   *
# *********************************************************************

import random


def to_chars(text):
    """
    Description: Turns a string into an array of characters.
    Parameters:  text (str) - the text the user typed
    Returns:     list of single-character strings
    """
    chars = []              #empty list for characters
    for c in text:          #for loop for number of characters in the inputted text
        chars.append(c)     #add each letter c to list chars
    return chars            #return list chars


def to_text(chars):
    """
    Description: Builds a string from an array of characters using
                 concatenation (+), since string methods are not allowed.
    Parameters:  chars (list) - array of characters
    Returns:     str - the characters joined together
    """
    text = ""           #define empty string
    for c in chars:     #loop for number of characters in chars list
        text = text + c #text string is text and add the next letter in the list at the end
    return text         #return the reconstructed text


def is_letter(c):
    """
    Description: Checks whether a single character is a letter A-Z or a-z.
    Parameters:  c (str) - one character
    Returns:     bool - True if c is a letter
    """
    return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") #check if the character is in the range of lower or uppercase letters


def is_vowel(c):
    """
    Description: Checks whether a single character is a vowel (any case).
    Parameters:  c (str) - one character
    Returns:     bool - True if c is a, e, i, o, or u
    """
    return c in "aeiouAEIOU" #check if c character is a upper or lowercase vowel 


def to_lower(chars):
    """
    Description: Converts every uppercase letter to lowercase. Returns a
                 NEW array; the original is not changed.
    Parameters:  chars (list) - array of characters
    Returns:     list - lowercase copy of the array
    """
    result = []                                 #create empty list for result
    for c in chars:                             #for c in the list of characters
        if c >= "A" and c <= "Z":               #check if c is an uppercase letter
            result.append(chr(ord(c) + 32))     #add 32 to code of Uppercase letter to make the letter lowercase
            result.append(c)                    #value of c is already lowercase or is not a letter so there is nothing to change
    return result                               #return result list


def to_upper(chars):
    """
    Description: Converts every lowercase letter to uppercase. Returns a
                 NEW array; the original is not changed.
    Parameters:  chars (list) - array of characters
    Returns:     list - uppercase copy of the array
    """
    result = []                             #empty results list
    for c in chars:                         #for c in list of characters
        if c >= "a" and c <= "z":           #check if letter is lowercase
            result.append(chr(ord(c) - 32)) #subtract 32 from lowercase code to make letter uppercase
        else:
            result.append(c)                #if letter is already uppercase, add directly to list without changing it
    return result                           #return result list


def reverse_and_display(chars):
    """
    Description: Prints the characters in reverse order. The array itself
                 is not changed.
    Parameters:  chars (list) - array of characters
    Returns:     nothing (prints the result)
    """
    reversed_text = ""                              #reversed text empty string
    i = len(chars) - 1                              #start with last index of list 
    while i >= 0:                                   #while i is inside of the length of chars list
        reversed_text = reversed_text + chars[i]    #reversed_text is what is already inside and the new letter
        i = i - 1                                   #subtract 1 from i to cycle through next character                                   
    return reversed_text                            #return the new string


def count_vowels(chars):
    """
    Description: Counts all vowels (a, e, i, o, u) in any case.
    Parameters:  chars (list) - array of characters
    Returns:     int - total number of vowels
    """
    count = 0                                       #count is 0
    for c in chars:                                 #for c in characters list
        if is_vowel(c):                             #check if c is a vowel
            count = count + 1                       #if c is a vowel, add 1 to vowel count
    return count                                    #return final vowel count


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
    for c in to_lower(chars):           # compare against the lowercase copy of chars
        if c == target:                 #if c is equal to the target vowel
            count = count + 1           #count of that vowel increases by 1
    return count                        #return vowel count


def vowel_subtotals(chars):
    """
    Description: Counts each vowel separately.
    Parameters:  chars (list) - array of characters
    Returns:     list of 5 ints - counts for a, e, i, o, u (in that order)
    """
    vowels = "aeiou"                                    #define vowels
    counts = [0, 0, 0, 0, 0]                            #define vowel counts
    for i in range(5):                                  #for i in range of 5 different vowels
        counts[i] = count_one_vowel(chars, vowels[i])   #check if each vowels[i] appears
    return counts                                       #return vowel count


def count_consonants(chars):
    """
    Description: Counts all consonants (letters that are not vowels).
    Parameters:  chars (list) - array of characters
    Returns:     int - total number of consonants
    """
    count = 0                                   #define count
    for c in chars:                             #for c in list chars
        if is_letter(c) and not is_vowel(c):    #if c is a letter and is not a vowel
            count = count + 1                   #add one to count
    return count                                #return count


def consonant_subtotals(chars):
    """
    Description: Counts how many times each consonant appears (Bonus).
    Parameters:  chars (list) - array of characters
    Returns:     list of 26 ints - index 0 is 'a', 1 is 'b', ... 25 is 'z'.
                 Vowel positions stay 0.
    """
    counts = [0] * 26
    for c in to_lower(chars):                      #for c in lowecase converted chars list
        if is_letter(c) and not is_vowel(c):       #if 
            counts[ord(c) - ord("a")] += 1         # ord(c) - ord('a') turns a letter into a position 0-25
    return counts


def first_name(chars):
    """
    Description: Returns the first name (everything before the first space).
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the first name
    """
    first = []                  #list for first name
    for c in chars:             #for c in chars list
        if c == " ":            #if c is a space
            break               #break loop
        first.append(c)         #if c isnt a space add letter to list
    return first                #return first name


def last_name(chars):
    """
    Description: Returns the last name (everything after the last space).
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the last name, or an empty list if
                 the name is only one word
    """
    if " " not in chars:                #if there are no spaces
        return []                       #return empty list
    last = []                           #define last name list
    i = len(chars) - 1                  #work from back to fron until a space is reached
    while i >= 0 and chars[i] != " ":   
        last.insert(0, chars[i])        #insert at place 0 to make sure letters stay in order    
        i = i - 1                       #i is i minus one
    return last                         #return the last name list


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
    for i in range(len(chars)):         
        if chars[i] == " ":
            if first_space == -1:
                first_space = i
            last_space = i
    if first_space == last_space:   #if there is only one space
        return []                   #return empty list
    middle = []                     #define middle name list
    for i in range(first_space + 1, last_space):
        middle.append(chars[i]) #add letters between the first and last spaces to middle name
    return middle               #return middle name list


def last_has_hyphen(chars):
    """
    Description: Checks whether the last name contains a hyphen.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     bool - True if the last name has a '-'
    """
    for c in last_name(chars):  #for c is in the last name characters list
        if c == "-":            #if c is a hyphen
            return True         #return that last name has a hyphen
    return False                #if there are no hyphens return false


def scramble(chars):
    """
    Description: Mixes up the letters. This MODIFIES the array that is
                 passed in instead of returning a new one.
    Parameters:  chars (list) - array of characters (changed in place)
    Returns:     nothing
    """
    for i in range(len(chars)): #for loop in the range of the length of chars list
        j = random.randint(0, len(chars) - 1) #j is the random index between 0 and the second to last spot
        temp = chars[i]                       #these three lines swap char[i] and char[j]
        chars[i] = chars[j]
        chars[j] = temp

def first_is_palindrome(chars):
    """
    Description: Checks whether the first name reads the same forwards
                 and backwards, ignoring upper/lower case.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     bool - True if the first name is a palindrome
    """
    first = to_lower(first_name(chars))             #first is lowecase converted first name from chars list
    for i in range(int(len(first) / 2)):                #i in range of the length of first name divided by two
        #using / resulted in a 'float error' so i stuck with //, updated to turn the whole division result into an integer, that worked
        if first[i] != first[len(first) - 1 - i]:   #if first[i] does not equal the spot at the opposite end of the word
            return False                            #word is not a palindrome
    return True                                     #if the above statement is not true, then the word is a palindrome

def sorted_chars(chars):
    """
    Description: Returns the full name as a sorted array of characters.
                 Spaces are removed and letters are made lowercase so the
                 order is alphabetical. Uses bubble sort on a copy.
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - sorted characters
    """
    letters = []                    #letters is empty list of letters
    for c in to_lower(chars):       #for c in forced lower chars
        if c != " ":                #if c does not equal a space
            letters.append(c)       #add c to letters list
    for i in range(len(letters)):   # Bubble sort: each pass pushes the largest remaining character to the end, so the range of positions checked shrinks each pass
        for j in range(len(letters) - 1 - i):
            if letters[j] > letters[j + 1]:
                temp = letters[j]
                letters[j] = letters[j + 1]
                letters[j + 1] = temp
    return letters

def initials(chars):
    """
    Description: Makes initials from the name, e.g. "mary jane watson"
                 becomes "M.J.W." I know this is spiderman's girlfriend
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     list - characters of the initials
    """
    result = []                     #define empty list result
    new_word = True                 #True when the next letter starts a word
    for c in to_upper(chars):       #for c in forced uppercase chars list
        if c == " ":                #if c is a space
            new_word = True         #there is a new word
        elif new_word:              #add c to list of initials and add a period in between the initials
            result.append(c)
            result.append(".")
            new_word = False        #set new word to false
    return result                   #return result


# 15. Title check (Bonus)

def has_title(chars):
    """
    Description: Checks whether any word in the name is a title or
                 distinction such as Dr., Sir, Esq, or Ph.D (any case).
    Parameters:  chars (list) - array of characters holding the full name
    Returns:     bool - True if a title is found
    """
    titles = ["dr", "dr.", "sir", "esq", "ph.d", "mr", "mr.", "mrs",
              "mrs.", "ms", "ms."]          #possible title options
    word = ""                               #word is an empty string
    lowered = to_lower(chars)               #lowered is the chars list converted to lowecase
    lowered.append(" ")                     #add a space to the end of the list  
    for c in lowered:                       #for c in the lowered list
        if c == " ":                        #if c is a space
            if word in titles:              #check if the word is in titles
                return True                 #if the word matches the list, return boolean true
            word = ""                       #reset word            
        else:
            word = word + c                 #if c is not a space, 
    return False                            #if not a title, return false



def caesar(chars, shift):
    """
    Description: Encodes the text by moving each letter 'shift' places
                 along the alphabet, wrapping from z back to a. Output is
                 lowercase; non-letters are left alone.
    Parameters:  chars (list) - array of characters
                 shift (int) - number of places to move (negative decodes)
    Returns:     list - the encoded characters (a new array)
    """
    result = []               #
    for c in to_lower(chars): #for c in the forced lower chars
        if c >= "a" and c <= "z":
            # 1. ord(c) - ord('a') position in alphabet (0-25)
            # 2. + shift           moves letter forward forward
            # 3. % 26              wraps around past 'z'
            # 4. + ord('a')        converts back into a letter code
            result.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(c) #if not a letter, add back to list
    return result

def show_menu():
    """
    Description: Prints the list of menu options.
    Parameters:  none
    Returns:     nothing
    """
    print("\n--- MENU ---")     #print the menu
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
    Description: Asks for a name/word, then shows the menu and runs
                 the chosen function until the user enters 0.
    Parameters:  none
    Returns:     nothing
    """
    name = to_chars(input("Enter your name or a word: "))  #name is list form of the inputted string
    choice = ""                                            #choice is empty string
    while choice != "0":
        show_menu()                                        #displays menu
        choice = input("Choice: ")                         #choice is the input for the question asked
        if choice == "1":
            print(reverse_and_display(name))               #print reversed name/word
        elif choice == "2":
            print("Total vowels:", count_vowels(name))
            v = input("Which vowel do you want counted? ") #choose vowel to be counted
            if len(v) == 1 and is_vowel(v):                #confirm v is actually a vowel
                print(v, "appears", count_one_vowel(name, v), "times")  #print how many times v vowel appears
            else:
                print("That is not a vowel.")                           #if input is not a vowel print error message
            print("Subtotals for a e i o u:", vowel_subtotals(name))    #print subtotals for each vowel
        elif choice == "3":
            print("Total consonants:", count_consonants(name))          #total number of consonants
            counts = consonant_subtotals(name)                          #counts is subtotals of every consonant
            for i in range(26):                                         #for i in range of the alphabet
                if counts[i] > 0:
                    print(chr(ord("a") + i) + ":", counts[i]) #chr(ord('a') + i) turns position i back into a letter
        elif choice == "4":
            print(to_text(first_name(name))) #print results of first name function
        elif choice == "5":
            print(to_text(last_name(name)))  #print results of last name function
        elif choice == "6":
            print(to_text(middle_names(name))) #print results of middle name function
        elif choice == "7":
            print(last_has_hyphen(name)) #print results of hyphen checker function
        elif choice == "8":
            print(to_text(to_lower(name))) #print results of forced lowecase function
        elif choice == "9":
            print(to_text(to_upper(name))) #print results of forced uppercase function
        elif choice == "10":
            scramble(name)       #scramble the array
            print(to_text(name)) #print scrambled array
        elif choice == "11":
            print(first_is_palindrome(name)) #print results of palindrome checker function
        elif choice == "12":
            print(to_text(sorted_chars(name))) #print results of sorted characters function
        elif choice == "14":
            print(to_text(initials(name))) #print results of initials function
        elif choice == "15":
            print(has_title(name)) #print results of title check function
        elif choice == "17":
            shift = int(input("Shift by: "))        #choose shift factor for caeser cypher
            print(to_text(caesar(name, shift)))     #print cyphered code
        elif choice != "0":             #if the choice is not one of the available options print error message
            print("Invalid choice")
    print("Goodbye!")


main()