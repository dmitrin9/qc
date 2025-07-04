import pennylane as qml
from pennylane import numpy as np

def sort(thing):
    result = {}
    for _ in thing:
        biggest=("", 0)
        for i in thing:
            k=i
            v=thing[k]
            if v > biggest[1]:
                biggest=(k,v)
        result[biggest[0]]=biggest[1]
        thing[biggest[0]]=0
    return result


def compress(thing):
    ft = {}
    for _,c in enumerate(thing):
        try:
            ft[c]+=1
        except KeyError:
            ft[c]=1

    ft = sort(ft)
    return ft

if __name__ == "__main__":
    string = "HHelllo"
    compressed = compress(string)
    print(compressed)
