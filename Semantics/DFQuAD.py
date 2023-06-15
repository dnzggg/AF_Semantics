from AF import ArgumentationFramework


class DFQuAD:
    def __init__(self, af: ArgumentationFramework):
        self.af = af
        self.scores = {}

    def __str__(self):
        return str(self.af)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: 'DFQuAD'):
        return self.af == other.af

    def __hash__(self):
        return hash(self.af)

    def get_af(self):
        return self.af

    def set_af(self, af):
        self.af = af

    def compute_strength(self):
        for arg in self.af.get_arguments():
            self.scores[arg] = arg.get_base_score()

        for arg in self.af.get_arguments():
            for relation in self.af.get_relations():
                if relation.get_arg2() == arg:
                    if relation.get_attack():
                        self.scores[arg] = self.scores[arg] * (1 - self.scores[relation.get_arg1()])
                    else:
                        self.scores[arg] = self.scores[arg] * self.scores[relation.get_arg1()]

    def get_scores(self):
        return self.scores
