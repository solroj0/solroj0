"""
This program opens all the files in your directory, reads, and prints the wordcount.
It also prints out specific stats about how many words are in each document
It excludes files ending in .py to ommit programs
"""
import os

def count_words_in_file(file_path, filename):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0

def count_words_in_folder(folder_path):
    file_contents = []
    total_words = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not filename.endswith(".py") and os.path.isfile(file_path):
            word_count = count_words_in_file(file_path, filename)
            total_words += word_count
            file_contents.append([filename, word_count])
    return total_words, file_contents

if __name__ == "__main__":
    folder_path = os.path.dirname(__file__)  # Use the directory of the script
    output = count_words_in_folder(folder_path)
    print("-" * 60 + "\n" + f"Total words in the folder: {output[0]}")
    for things in output[1]:
        print(things)
    print("-"*60)
