from .Argument import Argument
from .Relation import Relation


class ArgumentationFramework:
    def __init__(self, arguments: [Argument], relations: [Relation]):
        self.arguments = arguments
        self.relations = relations

    def __str__(self):
        return "Arguments: " + str(self.arguments) + "\nAttacks: " + str(self.relations)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: 'ArgumentationFramework'):
        return self.arguments == other.arguments and self.relations == other.relations

    def __hash__(self):
        return hash((self.arguments, self.relations))

    def get_arguments(self):
        return self.arguments

    def get_relations(self):
        return self.relations

    def add_argument(self, argument: Argument):
        self.arguments.append(argument)

    def add_relation(self, relation: Relation):
        self.relations.append(relation)
