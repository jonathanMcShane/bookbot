with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def get_num_words(text):
    return len(text.split())

def get_letter_frequencies(text):
    letter_frequencies = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letter_frequencies:
            letter_frequencies[lowered] += 1
        else:
            letter_frequencies[lowered] = 1
    return letter_frequencies

def generate_report(letter_frequencies):
    frequency_list = list(letter_frequencies.items())
    frequency_list.sort(reverse = True, key = lambda x: x[1])
    for frequency in frequency_list:
        if frequency[0].isalpha():
            print(f"The '{frequency[0]}' character was found {frequency[1]} times")


number_words = get_num_words(file_contents)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{number_words} found in the document")
print ("")
generate_report(get_letter_frequencies(file_contents))
print("--- End report ---")
