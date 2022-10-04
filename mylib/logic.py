import wikipedia


def wiki(name="Ragnarok", length=1):
    """A Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
