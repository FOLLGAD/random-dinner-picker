from person import Person
from dinner import Dinner

def main():
    people = []
    while True:
        name = input("Enter a name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        cost = float(input(f"Enter the cost of {name}'s dinner: "))
        people.append(Person(name, cost))

    dinner = Dinner(people)
    payer = dinner.weighted_random_choice()
    print(f"{payer.name} should pay for the dinner.")

if __name__ == "__main__":
    main()
