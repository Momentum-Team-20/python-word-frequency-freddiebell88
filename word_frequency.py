import string

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


def remove_stop_words(word_list):
    no_stop_words = []
    for word in word_list:
        if word not in STOP_WORDS:
            no_stop_words.append(word)
    return no_stop_words


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    word_count = {}
    with open(file) as reader:
        text = reader.read()
        cleaned_text = remove_punctuation(text)
        words = cleaned_text.split()
        no_stop_words = remove_stop_words(words)
        print(no_stop_words)
        # print(string.punctuation)
        for word in no_stop_words:
            word = word.lower()
            # if word in word_dict:
            #     word_dict[word] = word_dict[word] + 1
            # else:
            #     word_dict[word] = 1
            word_count[word] = word_count.get(word, 0) + 1
    word_count_sorted = sorted(word_count.items(), key=lambda x:x[1])
    print(f'This is the sorted word count: {word_count_sorted}')
    word_count = dict(word_count_sorted)
    for key, value in word_count.items():
        print(key, value)


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
