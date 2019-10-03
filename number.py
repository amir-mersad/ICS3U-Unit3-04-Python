#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: Sep 2019
# This program checks if a number is positive, negative or 0


def main():
    # This function checks if a number is positive, negative or 0

    # Input
    number = int(input("Please enter a number (integer): "))

    # Process and Output
    if number < 0:
        print("-")
    elif number == 0:
        print(number)
    elif number > 0:
        print("+")
    else:
        pass


if __name__ == "__main__":
    main()
