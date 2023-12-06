def meal_test(answer):
    if answer == 1:
        print("Fried Chiken Yummy!")
    elif answer == 2:
        print("Burger")
    elif answer == 3:
        print("Pizza ")
    else:
        print("That is not an option!")
def main():
    print("which is your favorite meal?")
    print("1.Chicken")
    print("2.Burger")
    print("3.Pizza")
    answer = input()
    meal_test (int (answer))

if __name__ == "__main__":
    main()
