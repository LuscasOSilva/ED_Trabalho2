class Queue:
    def __init__(self, item):
        self.items = [[]]*item
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def colocar(self, item):
        self.items[len(self.items)-1] = self.items[len(self.items)-1] + [item]
    def peek(self):
        return self.items[len(self.items)-1]
    def peekUltimo(self):# pegando self[][]
        return self.items[len(self.items)-1][len(self.items[len(self.items)-1])-1]
    def size(self):
        return len(self.items)
    def show(self):
        return self.items
    
w = Queue(int(input()))
c = [int(x) for x in input().split()]
sobras = []
recebeu = 0
if w.show() == []:
    print(f'Os Wookies foram para o lado sombrio da força!')
    sobras = c
else:
    
    for i in c:
        l = 0
        recebeu = 0
        
        while l <= w.size() and recebeu == 0:
            if w.peek() == [] or w.peekUltimo() >= i:
                w.colocar(i)
                recebeu = 1
            w.enqueue(w.dequeue())
            l += 1
        
        if recebeu == 0:
            sobras.append(i)
    w = w.show()
    for i in range(len(w)):
        for l in range(len(w)-1,i,-1):
            if sum(w[i]) < sum(w[l]):
                w[i], w[l] = w[l], w[i]

    for i in w:
        print(f'{i}', end=' ')

    print('')
    
if len(sobras) == 0:
    print(f'A força está com os Wookies!')
else:
    for i in sobras:
        print(f'{i}', end=' ')
#do professor imundo
'''wookiees = [[] for _ in range(int(input()))]

cargas = [int(i) for i in input().split()]



sobras = []

for carga in cargas:

    if [] in wookiees:

        wookiees[wookiees.index([])].append(carga)

    else:

        for wookiee in wookiees:

            if wookiee[-1] >= carga:

                wookiee.append(carga)

                break

        else:

            sobras.append(carga)



if wookiees:

    print(*sorted(wookiees, key=lambda x: sum(x), reverse=True))

else:

    print('Os Wookies foram para o lado sombrio da força!')

if sobras:

    print(*sobras)

else:

    print('A força está com os Wookies!')'''