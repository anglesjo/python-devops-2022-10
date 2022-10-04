from unittest import result
import wikipedia


def wiki(name="Ragnarok", length=1):
    """A Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search Wikipedia for names"""
    
    result = wikipedia.search(name)
    return result