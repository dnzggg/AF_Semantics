from .Argument import Argument
from .Relation import Relation


class ArgumentationFramework:
    def __init__(self, arguments: {str: Argument} = None, relations: [Relation] = None):
        if arguments is None:
            arguments = {}
        if relations is None:
            relations = []
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
        return self.arguments.values()

    def get_relations(self):
        return self.relations

    def add_argument(self, argument: Argument):
        self.arguments[argument.name] = argument

    # def add_relation(self, relation: Relation):
    #     self.relations.append(relation)

    def add_relation(self, argument1: str, argument2: str, attack: bool):
        arg1 = self.arguments.get(argument1)
        arg2 = self.arguments.get(argument2)
        self.relations.append(Relation(arg1, arg2, attack))
