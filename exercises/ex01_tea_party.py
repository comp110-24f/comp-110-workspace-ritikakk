"""Program that helps plan tea party based on number of guests expected"""

__author__ = "730814121"


def main_planner(guests: int) -> None:
    """function that acts as the entrypoint of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """calculates how many tea bags will be needed based on the number of guests"""
    # num of people times 2 because each person drinks 2 cups of tea
    return people * 2


def treats(people: int) -> int:
    """calculates number of treats based on amount of tea guests drink"""
    # num of ppl must equal num of people for tea_bags function
    # tea_bags function output times 1.5; guests have 1.5 treats for each tea
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates overall cost of tea party based on cost of tea bags and treats"""
    # each cup of tea costs $0.50 and each treat costs $0.75
    # added together to find total cost of teas and treats
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
