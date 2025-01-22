from dataclasses import dataclass, field
from copy import copy

@dataclass
class AnimalNode:
    question: str
    yes_path: 'AnimalNode' = field(default=None)
    no_path: 'AnimalNode' = field(default=None)

    def article(self) -> str:
        return "an" if self.question[0].lower() in "aeiou" else "a"

    def full_name(self) -> str:
        return f"{self.article()} {self.question}"

    def is_leaf(self) -> bool:
        return self.yes_path is None and self.no_path is None

    def ask_question(self) -> bool:
        if not self.is_leaf():
            answer = input(f"Is it {self.full_name()}? ")
            print()

            if answer == "q" :
                return False
            
            if answer == "y":
                self.yes_path.ask_question() 
            else:
                self.no_path.ask_question()
        else:
            answer = input(f"Is it {self.full_name()}? ")

            if answer == "q" :
                return False
            
            if answer == "y":
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

                if new_answer == "y" :
                    self.yes_path = new_node
                    self.no_path = old_animal
                else:
                    self.yes_path = old_animal
                    self.no_path = new_node

            answer = input("Play again? ")
            print()
            return answer == "y"

