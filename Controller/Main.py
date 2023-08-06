from Model.wiki_google_api import wiki_google_api
class controller:

    def __init__(self):
        self.model=wiki_google_api()

    def query(self,key):
        return self.model.get(key)

    def change_language(self):
        self.model.set_lang()

