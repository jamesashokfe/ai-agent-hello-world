"""
A simple Echo Bot that repeats user input until the user types 'exit'.

This script implements a basic command-line echo bot that reads user input
and echoes it back until the user types 'exit' to quit the program.
"""


def main():
    """Main function to run the echo bot."""
    print("Echo bot is running. Type 'exit' to quit.")

    while True:
        user_query = input("User: ")
        if user_query.strip().lower() == "exit":
            print("Echo bot: Goodbye!")
            break
        print(f"Echo bot: {user_query}")


if __name__ == "__main__":
    main()
