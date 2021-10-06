class MemCalculator:
    __sum = 0

    def add(self, number):
        self.__sum += number
        pass
    
    def sum(self):
        temp = self.__sum
        self.__sum = 0
        return temp
