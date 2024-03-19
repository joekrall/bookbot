def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
        count_words(file_contents)
        count_letters(file_contents)

def count_words(f):
    words = f.split()
    print(f"{len(words)} words found in the document")

def count_letters(f):
    file_contents = f.lower().strip(" ")
    dictionary = {}
    for char in file_contents:
        if char.isalpha():
            if dictionary.get(char) == None:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_dictionary:
        print(f"The letter {item[0]} appears {item[1]} times")

main()
