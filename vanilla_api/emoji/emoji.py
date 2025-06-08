import pickle
import random

with open("./vanilla_api/emoji/emoji.pickle", "rb") as file:
    emoji = pickle.load(file)


def qwq():
    return random.choice(emoji)
