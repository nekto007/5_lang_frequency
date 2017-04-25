import sys
import collections
def load_data(filepath):
    with open(filepath, 'r') as listwords:
        text = listwords.read().split()
    return text


def get_most_frequent_words(text):
    topwords = []
    for i in text:
        if i.isalpha():
            topwords.append(i)
    topwords = collections.Counter(topwords).most_common(10)
    return topwords

if __name__ == '__main__':
    filepath = (sys.argv[1])
    text = load_data(filepath)
    topwords = get_most_frequent_words(text)
    print(('%s самых популярных слов: ' % (len(topwords))), topwords)
