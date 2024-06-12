# ------ 1 -------
import random
import string

# Create a list of letters
letters = list(string.ascii_lowercase)
#print(letters)

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

print("\nlist_of_dicts:")
print(list_of_dicts)

# ------ 2 --------
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
# Create final_dict with renamed keys
final_dict = {}
for key, (value, dict_number) in combined_dict.items():
    # Rename the key if it appears in more than one dictionary
    if sum(key in d for d in list_of_dicts) > 1:
        final_key = f"{key}_{dict_number}"
    else:
        final_key = key
    # Add the final key-value pair to the final_dict
    final_dict[final_key] = value

print("\nCombined dictionary:")
print(final_dict)