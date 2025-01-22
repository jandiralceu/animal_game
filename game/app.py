import os, sys

def main():
    print("Welcome to the animal game!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)