import json
class cache:

    def __init__(self):
        j= open("./Model/my_cache.json","r")
        self.data = json.load(j)
        j.close()

    def add(self,key,value):
        print("add to cache")
        if len(self.data)==100:
            first_key = next(iter(self.data))
            self.data.pop(first_key)
        self.data[key] = value
        with open("./Model/my_cache.json","w") as j:
            json.dump(self.data,j)

    def look_up(self,key):
        return self.data.get(key,False)
