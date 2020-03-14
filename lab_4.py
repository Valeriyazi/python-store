import pickle

class Clothes:
    def __init__(self, title = '', size = '', count = 0, price = 0):
        self.title = str(title)
        self.size = str(size)
        self.count = int(count)#количество
        self.price = float(price)#цена
        
def deleteArrayItem(pos, store):
    try:
        del store[pos]
    #если не удалено, значит элемента нет
    except IndexError:
        print("Такой вещи нет")


def saveArray(fname, store):
    with open(fname, "wb") as fout:
        for obj in store:
    #встроенная функция записи в подключенном модуле
            pickle.dump(obj, fout)

def loadArray(fname, store):
    try:
        with open(fname, "rb") as fin:
            while True:
                try:
    #встроенная функция загрузки в подключенном модуле
                    a = pickle.load(fin)
                    store.append(a)
                except EOFError:
                    return store
    except FileNotFoundError:
        return []
    
def findRecord(title, startSearchPos, store):
    current = startSearchPos
    while current < len(store) and store[current].title != title:
        current += 1
    return current

def itemArrayPrint(pos, store):
    print("|%s|%s|%d|%0.3f|" % (store[pos].title, store[pos].size, store[pos].count, store[pos].price))

def printTitleClothes(title, store):
    pos = findRecord(title, 0, store)
    while pos < len(store):
        itemArrayPrint(pos, store)
        print(pos)
        pos = findRecord(title, pos + 1, store)


store = []
while True:
#Ввод команды пользователем
    inp = input('d — delete clothes\na — add clothes\ns — search clothes\np — all clothes\nq — exit\n')
    #удаление
    if inp == 'd':
        deleteArrayItem(int(input('Введите номер вещи')), store)
    #добавление
    elif inp == 'a':
        store.append(Clothes(input("title:"), input("size:"), input("count:"), input("price:")))
        saveArray('test2.txt', store)
        
    elif inp == 's':
        printTitleClothes(input("Title: "),store)
    elif inp == 'p':
        if len(store):
            for i in range(len(store)):
                itemArrayPrint(i, store)
        else:
            print("Empty!!!")
    elif inp == 'q':
        break




