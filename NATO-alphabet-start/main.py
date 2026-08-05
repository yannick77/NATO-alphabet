
#Looping through dictionaries:

import pandas



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
#Loop through rows of a data frame
nato_dataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in nato_dataFrame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word: ").upper()
word_list = [nato_dictionary[letter] for letter in user_input]

print(word_list)



