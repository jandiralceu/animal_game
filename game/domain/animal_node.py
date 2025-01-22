from dataclasses import dataclass, field

@dataclass(frozen=True)
class AnimalNode:
    question: str
    yes_child: 'AnimalNode' = field(default=None)
    no_child: 'AnimalNode' = field(default=None)

    def article(self):
        pass

    def full_name(self):
        pass

    def is_leaf(self):
        pass

    def ask_question(self):
        pass
    