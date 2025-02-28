#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-02-23

# Calculates the dimensions of a rectangle


def main():
    # Gets length and width from user input
    length = int(input("Enter Length: "))
    width = int(input("Enter Width: "))
    # Calculates the perimeter and area
    area = length * width
    perimeter = 2 * (length + width)
    #prints the length, width, area and perimeter
    print("Length is:", length)
    print("Width is:", width)
    print("Area is:", area)
    print("Perimeter is:", perimeter)


if __name__ == "__main__":
    main()