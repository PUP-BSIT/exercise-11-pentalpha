from pyjokes import get_joke

def jokes():
    """Prints number of jokes based on user input"""
    user_input = input("How many jokes do you want to hear?: ")
    for user_input in range(int(user_input)):
        print(get_joke())