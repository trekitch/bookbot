# counts the words in the given text
def count_words(text):
    word_array = text.split()
    word_count = len(word_array)
    return word_count

# counts the letters of the given text
def count_letters(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["count"]

# sorts the dictionary of letter counts a return them 
def sort_counts(letter_dict):
    
    dict_list = []
    for k in letter_dict:
        new_dict = {}
        new_dict["letter"] = k
        new_dict["count"] = letter_dict[k]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
        
