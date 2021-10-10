# First Program
# Create a program that takes user input as strings and concatenates the strings
# with the correct grammar

def sentence_maker(phrase):
    questions = ("who", "what", "where", "why", "how")
    capitalized = phrase.capitalize()
    if phrase.startswith(questions):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))