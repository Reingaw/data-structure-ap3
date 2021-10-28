class Queue:
    def __init__(self):
        self.isOver = 0
        self.queue = []

    def Over(self):
        self.isOver = 1

    def lenght(self):
        return len(self.queue)

    def insertItem(self, value):
        if value <= 0:
            print('O número deve ser maior que zero!')
        elif self.lenght() >= 10:
            print('A fila está cheia, remova alguns items!')
        else:
            self.queue.append(value)

    def removeItem(self):
        if self.lenght() == 0:
            print('A fila está vazia, adicione alguns items!')
        else:
            self.queue.pop(0)

    def clearQueue(self):
        if self.lenght() == 0:
            print('A fila está vazia, adicione alguns items!')
        else:
            self.queue.clear()

    def showEvenNumbers(self):
        aux = []
        for num in self.queue:
            if num % 2 == 0:
                aux.append(num)
        self.queue = aux
        self.isOver = 1

sQueue = Queue()
isOver = 0
def chooseOption(option):
    if option == '1':
        value = input('Digite um numero maior que zero: ')
        sQueue.insertItem(int(value))
    elif option == '2':
        sQueue.removeItem()
    elif option == '3':
        sQueue.clearQueue()
    elif option == '4':
        sQueue.showEvenNumbers()
    elif option == '5':
        sQueue.Over()
    else:
        print('Opção Inválida!')

def printQueue():
    print('\n' * 2)
    print(sQueue.queue)
    print('\n' * 2)

while not isOver:
    option = input('1 - Adicionar \n'
                   '2 - Remover \n'
                   '3 - Limpar \n'
                   '4 - Finalizar e exibir números pares \n'
                   '5 - Finalizar programa \n'
                   'Escolha uma opção: ')
    chooseOption(option)
    printQueue()
    isOver = sQueue.isOver