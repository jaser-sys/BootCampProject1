class Products:


    def __init__(self, name,serealNum,weight , price):
        self.__name = name
        self.__serealNum = serealNum
        self.__weight = weight
        self.__price= price


    def set_name(self, name):
        self.__name = name

    def set_serealNum(self, serealNum):
        self.__serealNum = serealNum

    def set_weight(self, weight):
        self.__weight= weight

    def set_price(self, price):
        self.__price = price


    def get_name(self):
        return self.__name

    def get_serealNum(self):
        return self.__serealNum

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price



    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nSereal Num: ' + self.__serealNum + \
               '\nProduct Weight: ' + self.__weight + \
               '\nProduct Price: ' + self.__price