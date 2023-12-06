#!/usr/local/bin/python3

from username_checker import UserCheck

def main():

    username = input("Username: ")
    #username = "aji"
    if username == "":
        username = "aji"
  

    checker = UserCheck(username)
    checker.username_check()


if __name__ == "__main__":
    main()
