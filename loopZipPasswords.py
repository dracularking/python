import itertools
import zipfile

filename = "C:\\Users\\Administrator\\Desktop\\test.zip"


def uncompress(filename, password):
    try:
        with zipfile.ZipFile(filename) as zipFile:
            zipFile.extractall("./", pwd=password.encode('utf-8'))
        return True
    except:
        return False


chars = "abcdefghijklmnopqrstuvwxyz0123456789"
for c in itertools.permutations(chars, 4):
    password = "".join(c)
    password += "0000"
    result = uncompress(filename, password)
    if not result:
        print("unzip failed", password)
    else:
        print("unzip success", password)
        break


