import random


class ScientistsGenerator:

    adjetives = [
        "adaptable",
        "adventurous ",
        "friendly",
        "courageous ",
        "diligent ",
        "exuberant ",
        "gregarious ",
        "inventive",
        "passionate ",
        "person "
    ]
    scientists = [
        "Curie",
        "Turing",
        "Bohr",
        "Darwin",
        "daVinci",
        "Galilei",
        "Tesla",
        "Einstein",
        "Newton"
    ]

    @staticmethod
    def generate_name():
        adjetive = random.choice(ScientistsGenerator.adjetives)
        scientist = random.choice(ScientistsGenerator.scientists)
        random_name = "{}_{}".format(adjetive, scientist)
        return random_name