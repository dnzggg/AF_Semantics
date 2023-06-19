from AF import ArgumentationFramework


class DFQuAD:
    def __init__(self):
        self.scores = {}
        self.name = __class__.__name__

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def compute_strength(self, af: ArgumentationFramework):
        self.scores = {}

        converged = False
        while not converged:
            for argument in af.get_arguments():
                if argument.get_attackers() == [] and argument.get_supporters() == []:
                    self.scores[argument] = argument.get_base_score()
                else:
                    calc = True
                    attack_energy = 1
                    for attacker in argument.get_attackers():
                        if (score := self.scores.get(attacker)) is not None:
                            attack_energy *= (1 - score)
                        else:
                            calc = False
                    v_a = 1 - attack_energy

                    support_energy = 1
                    for supporter in argument.get_supporters():
                        if (score := self.scores.get(supporter))  is not None:
                            support_energy *= (1 - score)
                        else:
                            calc = False
                    v_s = 1 - support_energy

                    if calc:
                        v_0 = argument.get_base_score()
                        self.scores[argument] = v_0 + (0.5 + ((v_s - v_a) / (2 * abs(v_s - v_a))) - v_0) * abs(v_s - v_a)

            if len(self.scores) == len(af.get_arguments()):
                converged = True

    def get_scores(self):
        return self.scores
