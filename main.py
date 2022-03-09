class node():
    def __init__(self,value,key,left=None,right=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right
        self.code = ''


def sortare(d):
    return (d.value,d.key)


def citire(nume_fisier):
    f = open(nume_fisier)

    linii = f.readlines()
    d = {}
    for linie in linii:
        for elem in range(len(linie)):
            if linie[elem] in d:
                d[linie[elem]] = d[linie[elem]] + 1
            else:
                d[linie[elem]] = 1

    return d,"".join(linii)

def calculate(node,val=''):
    value = val + str(node.code)
    if node.left:
        calculate(node.left,value)
    if node.right:
        calculate(node.right,value)
    if not node.right and not node.left:
        arbore[node.key] = value

def huffman(d,nodes):
    for elm in d.keys():
        nodes.append(node(d[elm], elm))
    while len(nodes)>1:
        nodes = sorted(nodes,key=sortare)

        right = nodes[1]
        left = nodes[0]
        left.code = 0
        right.code =1

        new = node(right.value+left.value,right.key+left.key,left,right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new)

    calculate(nodes[0])

    return nodes


def codificare(text,arbore):
    list =[]
    for elm in text:
        list.append(arbore[elm])
    return "".join(list)

def cheie(val,arbore):
    for key,value in arbore.items():
        if val == value:
            return key
    return ""


def decodificare(text,arbore):
    list=[]
    cuv = text[0]
    k=0
    while len(text)>=0 and k<len(text):
        if cuv in arbore.values():
            c = cheie(cuv,arbore)
            list.append(c)
            if len(text) > k+1:
                text=text[k+1:]
                cuv = text[0]
            else:
                text=[]
            k=0
        else:
            k = k + 1
            cuv = cuv + text[k]
    return "".join(list)


d,text = citire("ff")
nodes = []
arbore =dict()

nodes=huffman(d,nodes)
text_cod = codificare(text,arbore)
print(f"Codul: {text_cod}")
text_decod = decodificare(text_cod,arbore)
print(f"Decodificare: {text_decod}")

