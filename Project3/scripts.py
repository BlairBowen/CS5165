import os
import socket
from collections import Counter

# File paths
file1 = "/home/data/IF.txt"
file2 = "/home/data/AlwaysRememberUsThisWay.txt"
output_dir = "/home/data/output"


def read_file(file_path):
    with open(file_path, "r") as file:
        text = file.read().replace("’", "'")  # Change apostrophe
        words = text.split()
        expanded_words = []
        for word in words:
            word = word.lower()
            word = word.replace("can't", "can not").replace("won't", "will not")
            word = word.replace("i'm", "i am").replace("don't", "do not")
            word = word.replace("i'll", "i will").replace("you've", "you have")
            word = word.replace("you'll", "you will").replace("'em", "them")
            word = word.replace("that's", "that is").replace("it's", "it is")
            word = word.replace("couldn't", "could not").replace("you're", "you are")
            expanded_words.extend(word.split())
        return expanded_words


def count_words(words):
    return len(words)


def top_frequent_words(words, top_n=3):
    counter = Counter(words)
    return counter.most_common(top_n)


def main():
    words_file1 = read_file(file1)
    words_file2 = read_file(file2)

    word_count_file1 = count_words(words_file1)
    word_count_file2 = count_words(words_file2)
    grand_total = word_count_file1 + word_count_file2

    top_3_file1 = top_frequent_words(words_file1)
    top_3_file2 = top_frequent_words(words_file2)

    ip_address = socket.gethostbyname(socket.gethostname())

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "result.txt")
    with open(output_file, "w") as f:
        f.write(f"Word count for IF.txt: {word_count_file1}\n")
        f.write(f"Word count for AlwaysRememberUsThisWay.txt: {word_count_file2}\n")
        f.write(f"Grand total word count: {grand_total}\n")
        f.write(f"Top 3 words in IF.txt: {top_3_file1}\n")
        f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_3_file2}\n")
        f.write(f"IP Address: {ip_address}\n")

    with open(output_file, "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
