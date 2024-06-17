# assign the value of the variable
input_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
# format text
normal_text = input_text.lower().replace('\n', '').replace('\u00A0', '')

#split text into sentences
split_text = normal_text.split('. ')

capitalize_split_text = []
last_words = []

for sentence in split_text:
    # Capitalize the first letter of the first word in every sentence
    capitalize_split_text.append(sentence.capitalize())
    # Split each sentence into words
    words = sentence.split()
    # Get last word in each sentence
    last_words.append(words[-1])

# Create sentence from last words and capitalize the first letter of the first word
last_words_string = ' '.join(last_words).capitalize()
# Create text from sentences
Normal_text = '. '.join(capitalize_split_text)
# Add sentence from last words to text and fix iz to is
final_text = (f"{Normal_text} {last_words_string}").replace('iz ', 'is ')
print(final_text)


whitespace_count = 0
for char in input_text:
    # check if char is whitespace_count
    if char.isspace():
        whitespace_count += 1

print(f"The number of whitespace characters in the text is: {whitespace_count}")