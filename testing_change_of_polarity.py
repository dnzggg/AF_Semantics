from AF import *
from Semantics import *

af = ArgumentationFramework()
af.add_argument(Argument(name="f1", base_score=0.5))
for i in range(47):
    af.add_argument(Argument(name="a" + str(i), base_score=0.0))
    af.add_relation("a" + str(i), "f1", False)

af.add_argument(Argument(name="a", base_score=1.0))
af.add_relation("a", "f1", False)

# for i in range(100):
#     af.add_argument(Argument(name="b" + str(i), base_score=1.0))
#     af.add_relation("b" + str(i), "f1", True)
af.add_argument(Argument(name="s", base_score=1.0))
af.add_relation("s", "f1", True)
print(af)

dfquad = DFQuAD()
dfquad.compute_strength(af)
scores = dfquad.get_scores()
scores_name = {argument.get_name(): scores[argument] for argument in scores}
scores.update(scores_name)
print(scores["f1"])
