import sys
def load_data(filepath):
    with open(filepath, 'r') as listwords:
        text = listwords.read()
    return text


def get_most_frequent_words(text):
    listwords = text.split()
    dictcountwords = {}
    topwords = []
    for i in set(listwords):
        if i.isalpha():
            dictcountwords[i] = listwords.count(i)
    for k,v in sorted(dictcountwords.items(), key=lambda x: x[1], reverse=True):
        topwords.append(k)
        if len(topwords) > 10:
            break
    return topwords

if __name__ == '__main__':
    filepath = (sys.argv[1])
    text = load_data(filepath)
    topwords = get_most_frequent_words(text)
    print('10 самых популярных слов: ', topwords)