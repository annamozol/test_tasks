from collections import Counter

bad_chars = ';,!:*,"().-_'


def word_count(file_path):
    with open(file_path, "r") as file:
        text = file.read()

    transl_table = str.maketrans("", "", bad_chars)
    cleaned_text = text.translate(transl_table).lower()
    list_of_words = cleaned_text.split()
    word_frequencies = Counter(list_of_words)
    result = "\n".join(f"{count} {word}" for word, count in word_frequencies.items())

    return result


if __name__ == '__main__':
    your_file_path = input("Enter your file path: ")
    print(word_count(your_file_path))
