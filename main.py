from AF import *
from Semantics import *

arguments = [Argument("a", base_score=0.2), Argument("b", base_score=0.6), Argument("c", base_score=0.8), Argument("d", base_score=0.2)]
relations = [Relation(arguments[0], arguments[1], attack=True), Relation(arguments[1], arguments[2], attack=False),
             Relation(arguments[2], arguments[3], attack=True)]
af = ArgumentationFramework(arguments, relations)
print(af)

dfquad = DFQuAD(af)
dfquad.compute_strength()
print(dfquad.get_scores())
