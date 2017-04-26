import sys
import re
import collections
def load_data(filepath):
    with open(filepath, 'r') as listwords:
        text = listwords.read()
        text = get_clean_string(text)
    return text


def get_most_frequent_words(text):
    topnumber= 10
    topwords = []
    for i in text:
        if i.isalpha():
            topwords.append(i)
    topwords = collections.Counter(topwords).most_common(topnumber)
    return topwords


def get_clean_string(text):
    text = re.sub(r'[^\w\s]', '', ' '.join(text.split())).lower().split(' ')
    return text

if __name__ == '__main__':
    filepath = (sys.argv[1])
    text = load_data(filepath)
    topwords = get_most_frequent_words(text)
    print(('%s самых популярных слов: ' % (len(topwords))), topwords)
