from AF import *
from Semantics import *

arguments = [Argument(name="d3", base_score=0.5), Argument(name="d1", base_score=1.0), Argument(name="d2", base_score=0.0), Argument(name="f1", base_score=0.5), Argument(name="d4", base_score=1.0)]
relations = [Relation(arguments[2], arguments[3], attack=True), Relation(arguments[1], arguments[3], attack=False),
             Relation(arguments[0], arguments[1], attack=True), Relation(arguments[4], arguments[0], attack=True)]
af = ArgumentationFramework(arguments, relations)
print(af)

dfquad = DFQuAD()
dfquad.compute_strength(af, intermediate=True)
scores = dfquad.get_scores()
scores_id = {argument.id: scores[argument] for argument in scores}
scores_name = {argument.get_name(): scores[argument] for argument in scores}
scores.update(scores_id)
scores.update(scores_name)
intermediate_scores = dfquad.get_intermediate_scores()
for argument in intermediate_scores:
    if argument.get_base_score() == 0:
        if intermediate_scores[argument]["v_a"] < intermediate_scores[argument]["v_s"]:
            print(argument)
            print("Irrationality detected")
    elif argument.get_base_score() == 1:
        if intermediate_scores[argument]["v_a"] > intermediate_scores[argument]["v_s"]:
            print(argument)
            print("Irrationality detected")
