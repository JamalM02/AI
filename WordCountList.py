#Q4
#Jamal Majadle 207513722


def word_count(file):
    lines_count = 0
    words_count = 0
    characters_count = 0
    with open(file) as f:
        for line in f:
            lines_count += 1
            line = line.strip()
            line = line.split()
            for word in line:
                if word.isalpha():
                    characters_count += len(word)
                    words_count += 1
    print("\tThere are:\n", lines_count, "Lines\n", words_count, "Words\n", characters_count
          , "Characters\n in file", file)


def word_frequency(file):
    words_count = 0
    wordslist = list()
    with open(file) as f:
        for line in f:
            line = line.strip()
            line = line.split()
            for word in line:
                if word.isalpha():
                    found = False
                    for item in wordslist:
                        if item['word'] == word:
                            item["count"] += 1
                            found = True
                            break
                    if not found:
                        wordslist.append({'word': word, 'count': 1})
    return wordslist


def top_words(topWords):
    top_count = 0
    sorted_word_counts = sorted(word_frequency("oliver_twist.txt"), key=lambda x: x['count'], reverse=True)
    print("\n\tTop " + str(topWords) + " words in oliver_twist.txt are:")
    for words in range(topWords):
        print(sorted_word_counts[words])


def top_counts(top_count):
    num_of_words = 0
    sorted_word_counts = sorted(word_frequency("oliver_twist.txt"), key=lambda x: x['count'], reverse=True)
    for counts in sorted_word_counts:
        if counts['count'] > top_count:
            num_of_words += 1
    print("\n\tnumber of words which appeared more than", top_count, "times is:", num_of_words)


word_count("oliver_twist.txt")
top_words(3)
top_counts(1000)
