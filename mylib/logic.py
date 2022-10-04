import wikipedia
from textblob import TextBlob


def wiki(name="Ragnarok", length=1):
    """A Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for names"""

    result = wikipedia.search(name)
    return result


def phrase(name):
    """Returns phrases from Wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
