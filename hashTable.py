# define Python user-defined exceptions
class HashTablError(Exception):
    """Base class for other exceptions"""
    pass


class HashTable:
    def __init__(self, length):
        self.length = length
        self.table = [None] * length

    def __repr__(self):
        rep = "The Hash Table is: " + str(self.table)
        return rep

    # Insert data into hash
    def __setitem__(self, key, value):
        index = hash(key) % self.length
        if not self.table[index]:
            self.table[index] = [(key, value)]
        else:
            for i in self.table[index]:
                try:
                    if i[0] == key:
                        raise HashTablError
                except HashTablError:
                    print("ERROR HashTbale: The Key, " + str(key) +
                          ", Exist Already in Hash Table")
                    return self.table
            self.table[index].append((key, value))
        return self.table

    # Serach data in table
    def __getitem__(self, key):
        index = hash(key) % self.length
        if not self.table[index]:
            try:
                raise HashTablError
            except:
                print("ERROR HashTable: The Key, " + str(key) +
                      ", is not stored in the Hash Table!")
                return None
        else:
            for i in self.table[index]:
                if i[0] == key:
                    return i[1]
            try:
                raise HashTablError
            except HashTablError:
                print("ERROR HashTable: The Key, " + str(key) +
                      ", is not stored in the Hash Table!")
                return None

    # Delete data
    def delete(self, key):
        index = hash(key) % self.length
        if not self.table[index]:
            try:
                raise HashTablError
            except:
                print("ERROR HashTable: The Key, " + str(key) +
                      ", is not stored in the Hash Table!")
        else:
            for count, i in enumerate(self.table[index]):
                # Check if array is length one
                if len(self.table[index]) == 1:
                    if i[0] == key:
                        temp = None
                        self.table[index], temp = temp, self.table[index]
                        return "Deleted:" + str(temp)
                else:
                    if i[0] == key:
                        return "Deleted:" + str(self.table[index].pop(count))
            try:
                raise HashTablError
            except HashTablError:
                print("ERROR HashTable: The Key, " + str(key) +
                      ", is not stored in the Hash Table!")


if __name__ == "__main__":
    badoo = HashTable(10)
    badoo["DeleGiwa"] = 1
    badoo["DeleGiwa2"] = 3
    badoo["DeleGiwa1"] = 2
    badoo["DeleGiwa3"] = 4
    badoo["DeleGiwa4"] = 5
    badoo["DeleGiwa5"] = 6
    badoo["DeleGiwa6"] = 7
    badoo["DeleGiwa7"] = 8
    badoo["DeleGiwa8"] = 9
    badoo["DeleGiwa9"] = 10
    badoo["DeleGiwa10"] = 11
    badoo["DeleGiwa11"] = 12
    badoo["DeleGiwa12"] = 13

    print(badoo)
    print(badoo.delete("DeleGiwa8"))
    print(badoo["DeleGiwa9"])
