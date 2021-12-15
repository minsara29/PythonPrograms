class Myint(int):
    n = 0

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        print(self.__str__())
        print(len(self.__str__()))
        if self.n < len(self.__str__()):
            result = self.__str__()[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration




if __name__ == '__main__':
    myint1 = Myint(356)
    myint2 = Myint(4)
    # print(myint1)
    # print(myint2)
    # print(myint1.n)
    # print(myint2.n)

    for digit in myint1:
        print(digit)
