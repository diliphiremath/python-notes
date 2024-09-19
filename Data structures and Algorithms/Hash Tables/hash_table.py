class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h +=  ord(char) # ord() function returns the Unicode code from a given characte
        return h % self.MAX  # Mod of number gives value inside the divided number

    def insert_item(self, key, value):
        location = self.get_hash(key)
        self.arr[location] = value
    
    def get_item(self, key):
        item_location = self.get_hash(key)
        return self.arr[item_location]
    
    def delete_item(self,key):
        item_location = self.get_hash(key)
        self.arr[item_location] = None
        
    # using operators
    def __setitem__(self, key, value):
        location = self.get_hash(key)
        self.arr[location] = value
    
    def __getitem__(self, key):
        item_location = self.get_hash(key)
        return self.arr[item_location]
    
    def __delitem__(self, key):
        item_location = self.get_hash(key)
        self.arr[item_location] = None


h = HashTable()
h.insert_item('dilip',30)
h.insert_item('appu',50)
h.insert_item('sammu',80)
print(h.get_item('sammu'))
h.delete_item('sammu')
print(h.get_item('sammu'))

# using operators
print("============Operators=============")
h['raju'] = 20
h['reema'] = 99
print(h['reema'])
del h['raju']
print(h['raju'])