def english_to_piglatin(word):
    '''english_to_piglatin(word) -> string
    Translates word into Pig Latin.'''
    word = word.lower()
    if word[0] in 'aeiou':  # check if the first letter is a vowel
        s = word[0]
        first_letter=s.upper()
        word = str(first_letter)+word[1:]
        return word+"way"
    # word begins with a consonant
    consonants = ''  # keep track of consonants at start of word
    while len(word) > 0 and word[0] not in 'aeiou':
        consonants += word[0]  # add the consonant
        word = word[1:]        # remove the first letter from word 
    final_answer= str(word + consonants + 'ay')
    s = final_answer[0]
    first_letter=s.upper()
    final_answer = str(first_letter)+final_answer[1:]
    return final_answer

word = str(input("What phrase would you like to convert to Pig Latin?\n"))
print("In Pig Latin, your phrase would be "+english_to_piglatin(word)+".")
