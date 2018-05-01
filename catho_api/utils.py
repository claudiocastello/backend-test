import unicodedata, re
from nltk.corpus import stopwords

portuguese_stopwords = set(stopwords.words('portuguese'))

def remove_accent_marks(text):
    """
    text -> string
    A solution provided by Rodrigo Boniatti (boniattirodrigo)
    based on a Stack Overflow answer.
    https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79
    http://stackoverflow.com/a/517974/3464573
    """
    # Unicode normalize changes a character in its Latin equivalent.
    nfkd = unicodedata.normalize('NFKD', text)
    no_accent_words = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Make use of regular expression to return the text with only numbers, letters and spaces
    return re.sub('[^a-zA-Z0-9 \\\]', '', no_accent_words)


def remove_stop_words(text_set):
    '''
    text_set -> set of strings
    Receive a set of words as parameter and
    remove portuguese stopwords from it.
    '''
    new_text = set()
    for word in text_set:
        if word not in portuguese_stopwords:
            new_text.add(word)
    return new_text


def normalize_text(text):
    '''
    text -> string
    
    Return a string with no portuguese stopwords and
    no accent marks.
    '''
    # Receive text as string parameter and set it to lowercase
    # and replace '.' with ' '
    lower_text = text.lower().replace('.', ' ')

    # Changes text into a set (remove duplicate words)
    text_set = set(lower_text.split(' '))

    # Remove </li>, <li> and </li><li> from the set, if present.
    to_remove = set(['</li>', '<li>', '</li><li>'])
    text_set = text_set.difference(to_remove)

    # Remove stopwords from the text set
    stopwords_removed = remove_stop_words(text_set)

    # Join stopwords_removed into a string
    joined_text = ' '.join(stopwords_removed)

    # Remove accent marks from the string
    no_accent_text = remove_accent_marks(joined_text)
    return no_accent_text
