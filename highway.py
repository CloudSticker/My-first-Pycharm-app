import random
import sys


class Car(object):
    def __init__(self, position, roadlen):
        self.position = position
        self.roadlen = roadlen-1

    def getPosition(self):
        return self.position

    def goForward(self):
        if self.roadlen == self.position:
            self.position = 0
        else:
            self.position = self.position + 1


class Road(object):
    def __init__(self, carsamount, roadlength):
        self.carsamount = carsamount
        self.roadlength = roadlength
        if self.carsamount > roadlength - 2:
            print("You can't have that much cars on this road")
            sys.exit()
        self.carsarray = []
        self.matrix = []
        self.outmatrix = [0]*roadlength

        i = 0
        while i < self.carsamount:
            self.rnum = random.randint(0, roadlength-1)
            if self.rnum in self.matrix:
                continue
            i = i + 1
            self.matrix.append(self.rnum)
            self.carsarray.append(Car(self.rnum, self.roadlength))
            self.outmatrix[self.rnum-1] = 1;

        print(self.outmatrix)

    def getMatrix(self):
        print(self.outmatrix)
        return self.outmatrix

    def makeMove(self):
        newmatrix = []
        for car in self.carsarray:
            temp = car.getPosition() + 1
            if temp == self.roadlength:
                temp = 0
            if temp not in self.matrix:
                self.outmatrix[car.getPosition() - 1] = 0
                car.goForward()
                self.outmatrix[car.getPosition() - 1] = 1
                newmatrix.append(car.getPosition())
                continue
            else:
                newmatrix.append(car.getPosition())
                continue
        self.matrix.clear()
        self.matrix = newmatrix
        print(self.outmatrix)
        return self.outmatrix



