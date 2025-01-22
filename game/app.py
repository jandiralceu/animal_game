import os, sys

from game.animal_node import AnimalNode

def main():
    # Initialize the tree.
    root = AnimalNode(question="platypus")

    # Display instructions.
    print('Answer y for Yes, n for No, and q for Quit\n')

    # Repeat until the user quits.
    while root.ask_question():
        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)