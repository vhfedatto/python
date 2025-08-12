class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, value):
        key = value % self.size
        index = self._hash_function(key)
        self.table[index].append(value)

    def get(self, key):
        index = self._hash_function(key)
        for val in self.table[index]:
            if val == key:
                return index
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash_function(key)
        for i, val in enumerate(self.table[index]):
            if val == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found")

    def imprimir(self):
        for index, bucket in enumerate(self.table):
            print(f"Posição {index}: {bucket}")