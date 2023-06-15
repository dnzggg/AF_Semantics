

class Argument:
    def __init__(self, name: str, base_score=0.5):
        self.name = name
        self.base_score = base_score

    def __str__(self):
        return self.name + "(sigma=" + str(self.base_score) + ")"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.base_score == other.base_score

    def __hash__(self):
        return hash((self.name, self.base_score))

    def get_name(self):
        return self.name

    def get_base_score(self):
        return self.base_score

    def set_base_score(self, base_score):
        self.base_score = base_score

    def set_name(self, name):
        self.name = name
