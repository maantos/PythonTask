class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getName() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getName() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setnextpin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class UnaryGate(LogicGate):
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getName() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setnextpin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NorGate(UnaryGate):
    def __init__(self, n):
        super(NorGate,self).__init__(n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setnextpin(self)

    def getTo(self):
        return self.togate

    def getFrom(self):
        return self.fromgate


def main():
    g1 = AndGate("G1")
    g2 = OrGate("G2")
    g3 = OrGate("G3")
    g4 = NorGate("G4")

    c2 = Connector(g2, g3)
    c1 = Connector(g1, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


if __name__ == '__main__':
    main()