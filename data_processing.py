#1 Prompt the user to enter a sentence and then print the sentence in uppercase letters.
sentence = input("Enter yours sentence: ")
formatted_sentence = sentence.upper()
print(formatted_sentence)
#2 Prompt the user to enter a paragraph and then count the number of words in the paragraph.
pharagraph = input("Enter pharagraph text: ")
formatted_pharagraph = len(pharagraph.split())
print(f"The pharagraph has {formatted_pharagraph} words.")
#3 Prompt the user for a string, and check if all the characters in the string are digits. Output true or false.
user_prompt = input("Enter string: ")
user_outcome = all(char.isdigit() for char in user_prompt.replace(" ",""))
print(f"In entered string characters are all digits: {user_outcome}")
#4 Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".
user_occurance = input("Enter words with letter 'a' to be modified for 'o' ")
occurance_modified = user_occurance.replace("a","o")
print(f"Modified version is: {occurance_modified}")
#5 Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.
user_names = input("Enter your name and surname: ")
names = user_names.split()
initials = [name[0] for name in names]
print(f"Your Initials are: ", "".join(initials))
#6 Prompt the user for a string, then print its length.
user_input = input("Enter a string: ")
count_input = len(user_input)
print(f"There are  {count_input} characters in your string.")