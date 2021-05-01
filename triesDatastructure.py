# define Python user-defined exceptions
class TriesError(Exception):
    """Base class for other exceptions"""

    def __init__(self, msg='Kindly review datastructure documentation', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.keyError = "ERROR Tries: The Key: " + \
            str(msg) + ", is not stored in the Tries!"


class Tries:
    def __init__(self, length):
        self.length = length
        self.table = {}

    def __repr__(self):
        rep = "The Tries is: " + str(self.table)
        return rep

    def get_dictList(self, dictionary):
        if not dictionary:
            return False
        else:
            lst = list(dictionary.keys())
            return lst

    def raise_key_error(self, key):
        try:
            raise TriesError(str(key))
        except TriesError as e:
            print(e.keyError)

    def __setitem__(self, key, value):
        tempDictA = self.table
        counter = 0

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            if not tempDictA:  # Trie is empty
                tempDictA.update({str(tempAscii): {}})
            elif counter == 1:  # First letter of key already in Tries
                # If first letter of key is in first level of Tries
                if str(tempAscii) in self.get_dictList(tempDictA):
                    if len(key) == 1:
                        tempDictA[str(tempAscii)].update({key: value})
                        return self.table  # Return imediately
                else:
                    if len(key) == 1:
                        tempDictA.update({str(tempAscii): {}})
                        tempDictA[str(tempAscii)].update({key: value})
                        return self.table  # Return imediately
                    else:
                        tempDictA.update({str(tempAscii): {}})
            elif counter > 1:
                tempDictB = {}
                for j in range(counter - 1):
                    if j == 0:
                        tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:  # Evaluate if this is the last key
                        try:  # Evaluate without error if node was previoduly created
                            if tempDictB[str(tempAscii)]:
                                tempDictB[str(tempAscii)].update({key: value})
                        except:
                            tempDictB.update({str(tempAscii): {}})

                            tempDictB[str(tempAscii)].update({key: value})

                # Evaluate if this is not the last key
                if j != len(key) - 2:
                    try:  # Evaluate without error if node was previoduly created
                        if not tempDictB[str(tempAscii)]:
                            tempDictB.update({str(tempAscii): {}})
                    except:
                        tempDictB.update({str(tempAscii): {}})

        return self.table

    def __getitem__(self, key):
        tempDictA = self.table
        counter = 0

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            # Evaluates if first letter of key is not in first node level
            if str(tempAscii) not in self.get_dictList(tempDictA) and counter == 1:
                self.raise_key_error(key)
            # Evaluates if first letter of key is in first node level
            elif counter == 1:
                if len(key) == 1:
                    return tempDictA[str(tempAscii)][key]
            # Evaluates for all nodes after the first
            else:
                tempDictB = {}
                for j in range(counter - 1):
                    if j == 0:
                        tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:  # Evaluate if this is the last key
                        if str(tempAscii) not in self.get_dictList(tempDictB):
                            self.raise_key_error(key)

                        else:
                            return tempDictB[str(tempAscii)][key]

                # Evaluate if this is not the last key
                if j != len(key) - 2:
                    if str(tempAscii) not in self.get_dictList(tempDictB):
                        self.raise_key_error(key)

        return self.table


if __name__ == "__main__":
    # Add items into try
    testObject = Tries(10)
    testObject["key"] = 1
    testObject["key"] = 2
    testObject["keyed"] = 3
    testObject["keyee"] = 4
    testObject["keyef"] = 5
    testObject["keyeg"] = 6
    testObject["keyeh"] = 7
    testObject["keyei"] = 8
    testObject["keyeidd"] = 10
    testObject["u"] = 9

    # Search for item previously added to Tries
    print(testObject["keyei"])

    # Search for item not previously added to Tries
    print(testObject["ku"])

    # Print objects in Tries Datastructure
    print(testObject)
