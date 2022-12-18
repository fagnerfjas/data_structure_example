
'''
    Um objeto do tipo ArrayList possui dois atributos:
    o array lista, que armazena os objetos e o inteiro tamanho, 
    que representa a quantidade de elementos presente na lista. 
    A classe ArrayList possui também uma constante CAPACIDADE_DEFAULT 
    que define em 20 a capacidade inicial da lista, 
    caso o programador não queira redefini-la. 
    Por fim, dois construtores são definidos: 
    um padrão, caso o programador não queira redefinir o tamanho inicial 
    da lista e um recebendo como parâmetro a capacidade desejada.

    Operações básicas: inserção, remoção e busca.
'''

class ArrayList: 

    a_list = []
    size = 0
    capacity = 0

    '''
    Constructor
    :return: void 
    '''
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.a_list = capacity * [None]


    def printList(self):
        print(self.a_list)


    '''
        insert the value in the next empty position and return true. 
        if not find empty position return false
        :param Object value
        :return Boolean 
    '''
    def add(self, value):
        index = 0
        for item in self.a_list:
            if item == None:
                self.a_list[index] = value
                self.size += 1
                return True
            index += 1
        return False 
    

    '''
        insert value in position setted on index variable
        :param undefined type value
        :param int index, default 0, define the position where it will be inserted
    '''
    def addIn(self, value, index=0):
        canPut = True
        if self.a_list[index] != None:
            canPut = self.rightShift(index)
        
        if canPut:
            self.a_list[index] = value
            self.size += 1
        return canPut


    def set(self, index, value):
        if(index >= 0 and index <= self.capacity):
            self.a_list[index] = value
            return True
        return False


    '''
        This method push elements for the next position until the last position,
        if the last position is filled, this method returm false.
        :return boolean
        :param int index, this is initial position for beging shift 
    '''
    def rightShift(self, index=0):
        if(index > self.capacity - 1):
            raise Exception('Index fora do tamanho esperado')
        if( self.a_list[-1] != None ):
            return False 
        
        item_to_next = self.a_list[index]
        self.a_list[index] = None
        while True:
            if( index == self.capacity-1 ):
                break
            else:
                aux = self.a_list[index + 1]
                self.a_list[index + 1] = item_to_next
                item_to_next = aux
            index += 1
        return True 
    

    def leftShift():
        return True


    '''
        Check if exist empty spaces.
        :return boolean
    '''
    def haveSpace(self):
        return self.size < self.capacity


    """
    Returm the number of elements in the
    List
    :return: int
    """
    def len(self):
        return self.size


    '''
        This method insert more empty spaces on the list
        increasing yuor capacity
        :param int amount, quantity of spaces that will be increased
    '''
    def addPosition(self, amount=1):
        for i in range(amount):
            self.a_list.append(None)
            self.capacity += 1
    
