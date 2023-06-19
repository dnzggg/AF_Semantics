from AF.Argument import Argument


class Relation:
    def __init__(self, arg1: Argument, arg2: Argument, attack: bool, weight=1):
        self.arg1 = arg1
        self.arg2 = arg2
        self.attack = attack
        self.weight = weight

        if self.attack:
            self.arg2.add_attacker(self.arg1)
        else:
            self.arg2.add_supporter(self.arg1)

    def __str__(self):
        return self.arg1.__str__() + (" ~> " if self.attack else " => ") + self.arg2.__str__() + (" (w=" + str(self.weight) + ")" if self.weight != 1 else "")

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.arg1 == other.arg1 and self.arg2 == other.arg2 and self.attack == other.attack and self.weight == other.weight

    def __hash__(self):
        return hash((self.arg1, self.arg2, self.attack, self.weight))

    def get_arg1(self):
        return self.arg1

    def get_arg2(self):
        return self.arg2

    def get_attack(self):
        return self.attack

    def get_weight(self):
        return self.weight

    def set_arg1(self, arg1):
        self.arg1 = arg1

    def set_arg2(self, arg2):
        self.arg2 = arg2

    def set_attack(self, attack):
        self.attack = attack

    def set_weight(self, weight):
        self.weight = weight
