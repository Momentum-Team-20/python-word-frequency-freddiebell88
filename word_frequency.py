import string
import pprint

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def remove_punctuation(str):
    for character in str:
        if character in string.punctuation:
            str = str.replace(character, "")
    return str


# function to remove stop words
def remove_stop_words(word_list):
    # empty list to put all words that are not stop words in
    no_stop_words = []
    for word in word_list:
        if word not in STOP_WORDS:
            no_stop_words.append(word)
    return no_stop_words


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    word_count = {}
    with open(file) as reader:
        # reading the file and putting that data into the variable called text
        text = reader.read()
        # removing punctuation from text
        cleaned_text = remove_punctuation(text)
        # splitting text string into a list
        words = cleaned_text.split()
        # calling function to remove stop words and
        # assigning it to the variable name no_stop_words
        no_stop_words = remove_stop_words(words)
        for word in no_stop_words:
            # making each word lowercare
            word = word.lower()
            # get each word in the word count and if it has been seen
            # before add 1 to it's count
            word_count[word] = word_count.get(word, 0) + 1
    # sorting list by word count ascending value
    word_count_sorted = sorted(word_count.items(), key=lambda x: x[1])
    # re-establishing word_count as a dictionary
    word_count = dict(word_count_sorted)
    for key, value in word_count.items():
        print(f'{key:>15} | {value} {value*'*'}')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
