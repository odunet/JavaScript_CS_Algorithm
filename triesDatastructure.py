# importing "copy" for copy operations
import copy


# define Python user-defined exceptions
class TriesError(Exception):
    """Base class for other exceptions"""

    def __init__(self, msg='Kindly review datastructure documentation', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class Tries:
    def __init__(self, length):
        self.length = length
        self.table = {}

    def __repr__(self):
        rep = "The Tries is: " + str(self.table)
        return rep

    def get_key(self, dictionary):
        if not dictionary:
            return False
        else:
            key = list(dictionary.keys())[0]
            return int(key)

    def get_dictList(self, dictionary):
        if not dictionary:
            return False
        else:
            lst = list(dictionary.keys())
            return lst

    def __setitem__(self, key, value):
        tempDictA = copy.deepcopy(self.table)
        counter = 0

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            if not tempDictA:
                tempDictA.update({str(tempAscii): {}})
            elif tempDictA and counter == 1:
                if tempAscii == self.get_key(tempDictA):
                    if len(key) == 1:
                        tempDictA[str(tempAscii)].update({key: value})
                else:
                    if len(key) == 1:
                        tempDictA.update({str(tempAscii): {}})
                    else:
                        tempDictA.update({str(tempAscii): {}})
                        tempDictA[str(tempAscii)].update({key: value})
            elif tempDictA and counter > 1:
                tempDictB = copy.deepcopy({})
                for j in range(counter - 1):
                    if j == 0:
                        tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:
                        try:
                            if tempDictB[str(tempAscii)]:
                                tempDictB[str(tempAscii)].update({key: value})
                        except:
                            tempDictB.update({str(tempAscii): {}})
                            tempDictB[str(tempAscii)].update({key: value})

                if j != len(key) - 2:
                    try:
                        if not tempDictB[str(tempAscii)]:
                            tempDictB.update({str(tempAscii): {}})
                            tempDict = copy.deepcopy(tempDictA)
                            tempDictB = copy.deepcopy({})
                            tempDictA = copy.deepcopy(tempDict)
                    except:
                        tempDictB.update({str(tempAscii): {}})
                        tempDict = copy.deepcopy(tempDictA)
                        tempDictB = copy.deepcopy({})
                        tempDictA = copy.deepcopy(tempDict)

        self.table = copy.deepcopy(tempDictA)
        return self.table

    def __getitem__(self, key):
        tempDictA = copy.deepcopy(self.table)
        counter = 0

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            if str(tempAscii) not in self.get_dictList(tempDictA) and counter == 1:
                try:
                    raise TriesError()
                except:
                    print("ERROR Tries: The Key, " + str(key) +
                          ", is not stored in the Tries!A")
                    error = TriesError()
                    return error
            elif str(tempAscii) in self.get_dictList(tempDictA) and counter == 1:
                if len(key) == 1:
                    return tempDictA[str(tempAscii)][key]
                else:
                    pass
            else:
                tempDictB = copy.deepcopy({})
                for j in range(counter - 1):
                    if j == 0:
                        tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:
                        if str(tempAscii) not in self.get_dictList(tempDictB):
                            try:
                                raise TriesError()
                            except:
                                print("ERROR Tries: The Key, " + str(key) +
                                      ", is not stored in the Tries!B")
                                error = TriesError()
                                return error
                        else:
                            return tempDictB[str(tempAscii)][key]

                if j != len(key) - 2:
                    if str(tempAscii) not in self.get_dictList(tempDictB):
                        try:
                            raise TriesError()
                        except:
                            print("ERROR Tries: The Key, " + str(key) +
                                  ", is not stored in the Tries!C")
                            error = TriesError()
                            return error

        self.table = copy.deepcopy(tempDictA)
        return self.table


if __name__ == "__main__":
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
    testObject["ke"] = 9

    print(testObject["keyei"])

    print(testObject["ab"])
