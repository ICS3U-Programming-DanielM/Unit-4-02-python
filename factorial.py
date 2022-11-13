# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 8, 2022
# this program uses a do..while loop/n
# to calculate the factorial of that number/n


def main():
    # define variables
    loop_counter = 0
    factorial_num = 1
    # get the user input
    User_Input = input("Enter a positive Integer: ")
    print()
    # process calculate the factorial 0f user input using a loop format
    try:
        User_Input_as_int = int(User_Input)
    except Exception:
        print()
        print("Please enter a positive integer : ")
        return main()
    if User_Input_as_int <= 0:
        print("Please enter a positive integer : ")
    else:
        while True:
            loop_counter = loop_counter + 1
            factorial_num = factorial_num * loop_counter
            print(" {} number of times through the loop.".format(loop_counter))
            if loop_counter >= User_Input_as_int:
                break
            print()
            print("{} is the factorial of {}.".format(factorial_num, User_Input_as_int))


if __name__ == "__main__":
    main()
