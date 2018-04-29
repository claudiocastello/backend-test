import unicodedata, re


def remove_accent_marks(text):
    """
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


def remove_stop_words(text):
    pass


def normalize_text(text):
    lower_case = text.lower()
    no_accent_text = remove_accent_marks(lower_case)
    # stopwords_removed = remove_stop_words(no_accent_text)
    return no_accent_text
