

class Argument:
    _counter = 0

    def __init__(self, ids=-1, name="", base_score=0.5):
        self.name = name
        self.base_score = base_score
        self.attackers = []
        self.supporters = []
        if ids < 0:
            Argument._counter += 1
            self.id = Argument._counter
        else:
            self.id = ids

    def __str__(self):
        return self.name if self.name != "" else str(self.id) + "(sigma=" + str(self.base_score) + ")"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.base_score == other.base_score

    def __hash__(self):
        return hash((self.name if self.name != "" else str(self.id), self.base_score))

    def get_name(self):
        return self.name

    def get_base_score(self):
        return self.base_score

    def set_base_score(self, base_score):
        self.base_score = base_score

    def set_name(self, name):
        self.name = name

    def add_attacker(self, attacker):
        self.attackers.append(attacker)

    def add_supporter(self, supporter):
        self.supporters.append(supporter)

    def get_attackers(self):
        return self.attackers

    def get_supporters(self):
        return self.supporters

    def get_id(self):
        return self.id
