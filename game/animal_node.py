"""
Main class 
"""

from dataclasses import dataclass, field
from copy import copy
from enum import Enum

class Answer(Enum):
    """User possible answers"""
    YES = "y"
    NO = "n"
    QUIT = "q"

@dataclass
class AnimalNode:
    """AnimalNode"""
    question: str
    yes_path: 'AnimalNode' = field(default=None)
    no_path: 'AnimalNode' = field(default=None)

    def article(self) -> str:
        """Return 'a' or 'an' depending on the first letter of the question."""
        return "an" if self.question[0].lower() in "aeiou" else "a"

    def full_name(self) -> str:
        """Return the full name of the animal."""
        return f"{self.article()} {self.question}"

    def is_leaf(self) -> bool:
        """Return True if the node is a leaf."""
        return self.yes_path is None and self.no_path is None

    def ask_question(self) -> bool:
        """Ask a question and return True if the user wants to play again."""
        if not self.is_leaf():
            answer = input(f"Is it {self.full_name()}? ")
            print()

            if answer == Answer.QUIT.value:
                return False

            if answer == Answer.YES.value:
                self.yes_path.ask_question()
            else:
                self.no_path.ask_question()
        else:
            answer = input(f"Is it {self.full_name()}? ")

            if answer == Answer.QUIT.value:
                return False

            if answer == Answer.YES.value:
                print("I won!😎\n")
                print()
            else:
                animal = input("I give up. What is it? ")
                new_node = AnimalNode(question=animal)
                print()
                new_question = input(f"What question can I ask to differentiate between {self.full_name()} and {new_node.full_name()}? ")
                print()
                new_answer = input(f"What is the answer for {new_node.full_name()}? ")

                old_animal = copy(self)
                self.question = new_question

                if new_answer == Answer.YES.value:
                    self.yes_path = new_node
                    self.no_path = old_animal
                else:
                    self.yes_path = old_animal
                    self.no_path = new_node

            answer = input("Play again? ")
            print()
            return answer == Answer.YES.value
