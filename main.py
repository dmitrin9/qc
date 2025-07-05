import pennylane as qml
from pennylane import numpy as np

class Node:
    def __init__(self, freq, letter=None):
        self.letter=letter
        self.freq=freq
    def __repr__(self):
        return f"Letter:{self.letter}, Freq:{self.freq}"

def sort(thing):
    result={}
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

def ccompression_table(thing):
    #     0     1        0     1       0     1       0
    # {(node1, node2), (sum, node3), (sum, node4), (sum)}
    huffman_tree=[]

    ft = {}
    for _,c in enumerate(thing):
        try:
            ft[c]+=1
        except KeyError:
            ft[c]=1

    ft = sort(ft)
    i=0
    n1=None
    n2=None
    for k,v in reversed(ft.items()):
        match i:
            case 0:
                n1=Node(v,k)
            case 1:
                n2=Node(v,k)
                huffman_tree.append((n1, n2))
            case _:
                previous_sum = huffman_tree[-1][0].freq + huffman_tree[-1][1].freq
                n1=Node(previous_sum)
                n2=Node(v,k)
                huffman_tree.append((n1, n2))
        i+=1
    previous_sum = huffman_tree[-1][0].freq + huffman_tree[-1][1].freq
    huffman_tree.append((Node(previous_sum),))

    # {"node3":"001", etc...}
    huffman_table={}
    for _,c in enumerate(thing):
        ch=0
        for pair in huffman_tree[-2::-1]:
            if pair[1].letter == c:
                ch+=1
                break
            else:
                ch+=1
        binary_value = bin(ch)[2:].zfill(2)
        huffman_table[c]=binary_value

    string_buffer=""
    for c in thing:
        string_buffer+=huffman_table[c]
    return (string_buffer, huffman_table)

if __name__ == "__main__":
    string = "HHelllo"
    huffman_table = ccompression_table(string)
    print(huffman_table)
