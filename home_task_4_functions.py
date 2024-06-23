# refactor task 2
# part 1 without changes because I already used function

import random
import string
# Create a list of letters
letters = list(string.ascii_lowercase)

# Function to create a random dictionary
def create_random_dict():
    # Random number of keys in the dictionary
    num_keys = random.randint(2, 5)
    # Select random letters as keys
    keys = random.sample(letters, num_keys)
    # Create a dictionary with random values (from 0 to 100)
    return {key: random.randint(0, 100) for key in keys}

# Create a list of a random number of dictionaries (from 2 to 5)
num_dicts = random.randint(2, 10)
list_of_dicts = [create_random_dict() for _ in range(num_dicts)]

print("---------- refactor task 2: ----------")
print("\nlist_of_dicts:")
print(list_of_dicts)


# part 2 added 2 functions
def create_combined_dict(list_of_dicts):
    combined_dict = {}
    # Iterate over each dictionary in the list with its index
    for dict_number, current_dict in enumerate(list_of_dicts, start=1):
        for key, value in current_dict.items():
            if key in combined_dict:
                # If the key already exists in the combined_dict, compare the values
                existing_value, existing_dict_number = combined_dict[key]
                if value > existing_value:
                    # Update the value and the dictionary number if the current value is greater
                    combined_dict[key] = (value, dict_number)
            else:
                # If the key does not exist, add it to the combined_dict
                combined_dict[key] = (value, dict_number)
    return combined_dict


combined_dict = create_combined_dict(list_of_dicts)


# Create final_dict with renamed keys
def create_final_dict(combined_dict):
    final_dict = {}
    for key, (value, dict_number) in combined_dict.items():
        # Rename the key if it appears in more than one dictionary
        if sum(key in d for d in list_of_dicts) > 1:
            final_key = f"{key}_{dict_number}"
        else:
            final_key = key
        # Add the final key-value pair to the final_dict
        final_dict[final_key] = value
    return final_dict


print("\nCombined dictionary:")
print(create_final_dict(combined_dict))

# refactor task 3
# assign the value of the variable
homework_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# function for format text
def final_text(input_text):
    normal_text = input_text.lower().replace('\n', '').replace('\u00A0', '')
    # split text into sentences
    split_text = normal_text.split('. ')
    capitalize_split_text = []
    for sentence in split_text:
        # Capitalize the first letter of the first word in every sentence
        capitalize_split_text.append(sentence.capitalize())
    # Create text from sentences
    capitalize_text = '. '.join(capitalize_split_text)
    final_text = (f"{capitalize_text}").replace('iz ', 'is ')
    return final_text

# function for creation text from last words
def last_words_text(input_text):
    normal_text = input_text.lower().replace('\n', '').replace('\u00A0', '')
    # split text into sentences
    split_text = normal_text.split('. ')
    last_words = []
    for sentence in split_text:
        # Split each sentence into words
        words = sentence.split()
        # Get last word in each sentence
        last_words.append(words[-1])
    # Create sentence from last words and capitalize the first letter of the first word
    last_words_string = ' '.join(last_words).capitalize()
    # Add sentence from last words to text and fix iz to is
    return last_words_string


# function to calculate number of whitespace characters in text
def whitespace_count(input_text):
    count = 0
    for char in input_text:
        # check if char is whitespace_count
        if char.isspace():
            count += 1
    return count

print("---------- refactor task 3: ----------")
print(final_text(homework_text),last_words_text(homework_text))
print(f"The number of whitespace characters in the text is: {whitespace_count(homework_text)}")