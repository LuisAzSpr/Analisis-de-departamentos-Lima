import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')


def obtener_frecuencias(textos, n=10, idioma='spanish'):
    """
    Recibe una lista de textos y devuelve las n palabras más repetidas.

    :param textos: Lista de strings con los textos a analizar.
    :param n: Número de palabras más repetidas a devolver.
    :param idioma: Idioma de las stopwords a eliminar (por defecto 'spanish').
    :return: Lista de tuplas (palabra, frecuencia).
    """
    # Concatenamos todos los textos en uno solo
    texto_completo = ' '.join(textos).lower()

    # Tokenizamos el texto
    tokens = word_tokenize(texto_completo)

    # Filtramos puntuación y stopwords
    stop_words = set(stopwords.words(idioma))
    tokens_filtrados = [word for word in tokens if word.isalpha() and word not in stop_words]

    # Contamos la frecuencia de las palabras
    frecuencias = Counter(tokens_filtrados)

    # Retornamos las n palabras más frecuentes
    return frecuencias.most_common(n)


def diferencias(frecuencias1, frecuencias2):
    return set(dict(frecuencias1).keys()) - set(dict(frecuencias2).keys())



