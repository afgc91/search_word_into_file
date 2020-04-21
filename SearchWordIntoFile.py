#!/usr/bin/python
import sys


def main():
    file_path = sys.argv[1]
    word_to_search = sys.argv[2]
    search_word_into_file(file_path, word_to_search)


def search_word_into_file(file_path, word_to_search):
    with open(file_path, 'r') as file:
        words = file.read().replace('\n', '\n ').split(' ')
        occurrences = 0
        matched_words = ''
        for x in range(len(words)):
            if word_to_search in words[x]:
                occurrences += 1
                matched_words += str(x) + ','
        print(f'The "{file_path}" file has {len(words)} words.')
        print(f'The word "{word_to_search}" is present in {occurrences} of the {len(words)} words in the file')
        print(f'Matched words indexes of the word "{word_to_search}": {matched_words}')


if __name__ == '__main__':
    main()
