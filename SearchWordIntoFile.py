#!/usr/bin/python
import sys


def main():
    file_path = sys.argv[1]
    word_to_search = sys.argv[2]
    search_word_into_file(file_path, word_to_search)


def search_word_into_file(file_path, word_to_search):
    with open(file_path, 'r') as file:
        words = file.read().split('\n')
        occurrences = 0
        matched_words = ''
        for x in range(len(words)):
            if word_to_search in words[x]:
                print(words[x])


if __name__ == '__main__':
    main()
