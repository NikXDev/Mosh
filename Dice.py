import random


class ClsDice:
    def fundice(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)   # return first, second (can also be used)
        return f'({first}, {second })'


dice = ClsDice()
print(dice.fundice())
