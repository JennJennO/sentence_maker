# First Program
# Create a program that takes user input as strings and concatenates the strings
# with the correct grammar

def sentence_maker(phrase):
    questions = ("who", "what", "where", "why", "how")
    capitalized = phrase.capitalize()
    
    results = []
    while True:
        user_input = input("Type something: ")
        if phrase.lower().startswith(questions):
            return "{}?".format(capitalized)
        elif user_input.strip() == "":
            print("You didn't type anything. Try again.")
        else:
            return "{}.".format(capitalized)

    print(" ".join(results))
