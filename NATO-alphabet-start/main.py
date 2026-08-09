
#Looping through dictionaries:

import pandas



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#Loop through rows of a data frame
nato_dataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in nato_dataFrame.iterrows()}

def generate_phonetic_alphabet():
    # Create a list of the phonetic code words from a word that the user inputs.
    user_input = input("Please enter a word: ").upper()
    try:
        word_list = [nato_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Please enter only letter in the alphabet")
        generate_phonetic_alphabet()
    else:
        print(word_list)

generate_phonetic_alphabet()


