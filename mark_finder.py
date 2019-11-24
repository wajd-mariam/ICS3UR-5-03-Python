# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: November 2019
# This program is MARK FINDER for students in Ontario


def percentage(level_string):
    # this function find the percentage of the mark entered
    # the list of levels and its corresponding percentage
    if level_string == "4+":
        percent = 97
    elif level_string == "4":
        percent = 90
    elif level_string == "4-":
        percent = 83
    elif level_string == "3+":
        percent = 78
    elif level_string == "3":
        percent = 74
    elif level_string == "3-":
        percent = 71
    elif level_string == "2+":
        percent = 68
    elif level_string == "2":
        percent = 64
    elif level_string == "2-":
        percent = 61
    elif level_string == "1+":
        percent = 58
    elif level_string == "1":
        percent = 54
    elif level_string == "1-":
        percent = 51
    elif level_string == "0+":
        percent = 45
    elif level_string == "0":
        percent = 35
    elif level_string == "0-":
        percent = 15
    else:
        percent = -1

    return percent


def main():
    # input
    level = input("Please enter your mark to show percentage: ")

    # calling functions
    percent1 = percentage(level)

    # output
    if percent1 == -1:
        print("Invalid mark, please try again")
    else:
        print("Your percentage is: {}%".format(percent1))


if __name__ == "__main__":
    main()
