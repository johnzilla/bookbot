# main.py

def count_words(book):

    # initialize a counter
    words = 0

    # loop through the text and count characters
    for i in book.split():
        words += 1
    
    return words

def count_chars(book):
    
    # set up an empty dict
    counts_dict = {}

    # set to lowercase
    lowered_string = book.lower()
    
    # count each character
    for c in list(lowered_string):
        if c not in counts_dict:
            counts_dict[c] = 0
        counts_dict[c] += 1

    return counts_dict

def main():

    # initialize vars
    words = 0
    counted_chars = {}
    sorted_letters = {}

    # read the Frankenstein file from disk
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
   
    # count words
    words = count_words(file_contents)
    
    # count chars
    counted_chars = count_chars(file_contents)
    
    # print output
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(words) + " words found in the document")

    # check print chars and char count sorted
    for k, v in counted_chars.items():
        if k.isalpha():
            sorted_letters[k] = v

    for w in sorted(sorted_letters, key=sorted_letters.get, reverse=True):
        print(w, sorted_letters[w])

    print("--- End report ---")
    # end output

if __name__ == "__main__":
    main()
