from AF import *
from Semantics import *

arguments = [Argument(name="d3", base_score=0.5), Argument(name="d1", base_score=1.0), Argument(name="d2", base_score=0.0), Argument(name="f1", base_score=0.5)]
relations = [Relation(arguments[2], arguments[3], attack=True), Relation(arguments[1], arguments[3], attack=False),
             Relation(arguments[0], arguments[1], attack=True)]
af = ArgumentationFramework(arguments, relations)
print(af)

dfquad = DFQuAD()
dfquad.compute_strength(af)
scores = dfquad.get_scores()
scores_id = {argument.id: scores[argument] for argument in scores}
scores.update(scores_id)
scores_name = {argument.name: scores[argument] for argument in scores}
scores.update(scores_name)
