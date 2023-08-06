import wikipedia
from googlesearch import search
from Model.cache import cache


class wiki_google_api:

    def __init__(self):
        self.cache = cache()
        self.lang = "en"

    def set_lang(self):
        if self.lang == "en":
            self.lang = "he"
        else:
            self.lang = "en"
        wikipedia.set_lang(self.lang)

    def wiki_search(self, key):
        try:
            page = wikipedia.page(key)
            summery = page.summary
            return summery
        except Exception:
            return False

    def google_search(self, key):
        result = search(key, num_results=3)
        for res in result:
            return res

    def get(self, key):
        cache_search = self.cache.look_up(key)
        if cache_search:
            print("found in cache")
            return cache_search
        wiki_search= self.wiki_search(key)
        if wiki_search:
            self.cache.add(key,wiki_search)
            return wiki_search
        google_search = self.google_search(key)
        self.cache.add(key, google_search)
        return google_search


