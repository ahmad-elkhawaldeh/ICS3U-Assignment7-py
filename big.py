# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program gives you the lagrest number in a list


def myMax(list1):
    max = list1[0]
    for number in list1:
        if number > max:
            max = number
    return max


def main():
    list1 = []
    num = int(input("Enter number of elements in list: "))
    while num <= 0:
        num = int(input("Enter valid number of elements, Try again: "))

    for loop in range(1, num + 1):
        elements = int(input("Enter elements: "))
        list1.append(elements)
    print("Largest element is:", max(list1))


if __name__ == "__main__":
    main()
