import random
from typing import List
from person import Person

class Dinner:
    def __init__(self, people: List[Person]):
        self.people = people

    def weighted_random_choice(self) -> Person:
        """
        Select a person randomly, with the probability of being selected
        weighted by the cost of their dinner.
        """
        total_cost = sum(person.dinner_cost for person in self.people)
        random_choice = random.uniform(0, total_cost)
        current_sum = 0
        for person in self.people:
            current_sum += person.dinner_cost
            if random_choice <= current_sum:
                return person
