#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-02-23

# Calculates the dimensions of a rectangle


def main():
    length = int(input("Enter Length: "))
    width = int(input("Enter Width: "))

    area = length * width
    perimeter = 2 * (length + width)

    print("Length is:", length)
    print("Width is:", width)
    print("Area is:", area)
    print("Perimeter is:", perimeter)

if __name__ == "__main__":
    main()

