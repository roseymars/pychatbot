import random


def random_string():
    random_list = [
        "Hmm, I'm having trouble understanding. Try writing something more descriptive.",
        "I don't understand this yet, hopefully I will in the future :)",
        "Could you please rephrase that?",
        "My bot brain is having a little trouble... please ask me something else",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]

print(random_string())