# Q4
# Jamal Majadle 207513722
import re


# Function to calculate the amount of: Lines, Words(counts once each word) and Characters in file
def word_count(file):
    lines_count = 0
    wordslist = list()
    characters_count = 0
    with open(file, 'r') as f:
        for line in f:
            lines_count += 1
            line = line.strip()
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                if word.isalpha():
                    found = False
                    for item in wordslist:
                        if item == word:
                            found = True
                            break
                    if not found:
                        wordslist.append(word)
                characters_count += len(word)
    print("\tThere are:\n", lines_count, "Lines\n", len(wordslist), "Words\n", characters_count
          , "Characters\n in file", file)


# Function that creat new objects from Dictionary type and store those objects in a list for farther use
def word_frequency(file):
    words_count = 0
    wordslist = list()
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                found = False
                for item in wordslist:
                    if item['word'] == word:
                        item['count'] = item['count'] + 1
                        found = True
                        break
                if not found:
                    wordslist.append({'word': word, 'count': 1})
    return wordslist


# Function to calculate and print received list for Top X count words
def top_words(topWords):
    top_count = 0
    sorted_word_counts = sorted(word_frequency("oliver_twist.txt"), key=lambda x: x['count'], reverse=True)
    print("\n\tTop " + str(topWords) + " words in oliver_twist.txt are:")
    for words in range(topWords):
        print(sorted_word_counts[words])


# Function to calculate and print received list for the number of words that appeared more than X times
def top_counts(top_count):
    num_of_words = 0
    sorted_word_counts = sorted(word_frequency("oliver_twist.txt"), key=lambda x: x['count'], reverse=True)
    for word in sorted_word_counts:
        if word['count'] > top_count:
            num_of_words += 1
    print("\n\tnumber of words which appeared more than", top_count, "times is:", num_of_words)


# tests
word_count("oliver_twist.txt")
top_words(3)
top_counts(1000)
