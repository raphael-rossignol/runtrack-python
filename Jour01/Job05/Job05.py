import string


def listAlphabet():
    return sorted(string.ascii_lowercase, reverse=True)


print(listAlphabet())