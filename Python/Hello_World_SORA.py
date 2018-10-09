import os
from collections import Counter


def main():
    Data = list()
    for woot, dirs, files in os.walk(".."):
        [Data.append(i.split(".")[0]) for i in files if i.split(".")[0] != ""]
    Temp = Counter(i[0] for i in Data)
    Temp = [i.replace("_", "")
            for i in Data if i[0] == max(Temp, key=Temp.get)]
    Temp = Counter(i for i in Data)
    Temp = max(Temp, key=Temp.get)
    print(Temp[:5].capitalize(), Temp[5:].capitalize()+"!")


if __name__ == "__main__":
    main()
