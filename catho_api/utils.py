import unicodedata
import re


def remove_accent_marks(word):
    """
    A solution provided by Rodrigo Boniatti (boniattirodrigo)
    based on a Stack Overflow answer.
    https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79
    http://stackoverflow.com/a/517974/3464573
    """
    # Unicode normalize changes a character in its Latin equivalent.
    nfkd = unicodedata.normalize('NFKD', word)
    no_accent_word = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', no_accent_word)
