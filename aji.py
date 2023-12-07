#!/usr/local/bin/python3

from uc import UserCheck
from rich import print
import signal
import sys

sys.path.append('discovery/network')
from ping import icmp_ping, tcp_ping, udp_ping, port_check

def signal_handler(sig, frame):
    print("\nCtrl+C Detected. Exiting Gracefully.")
    # Clean Processes securely here before exiting.
    # This will be a future update
    sys.exit(0)


# Main Menu User will see when ran Interactively
def display_main_menu():
    print("Welcome to the Aji Security OSINT Tool")
    print("Choose which of the below tools you want to use")
    print("1. Username Checker")
    print("2. Network Discovery")


def display_network_menu():
    print("Choose which Network Option you'd like to use")
    print("1. Ping")
    print("2. Back to Main Menu")


def display_ping_menu():
    print("Choose which Type of Ping you'd like to do")
    print("1. ICMP")
    print("2. TCP")
    print("3. UDP")
    print("4. Change IP")
    print("5. Back")


def ping_menu():
    ip = input("IP to ping: ")

    while True:
        display_ping_menu()
        choice = input(">>> ")
        if choice == "1":
            icmp_ping(ip)
        elif choice == "2":
            port = input("Port: (default '80'): ")
            if port == '':
                port = '80'
            port_check(port)
            if tcp_ping(ip, port):
                print(f"[bold green]Response[/bold green] from [bold cyan]{ip}[/bold cyan]")
        elif choice == "3":
            udp_ping()
        elif choice == "4":
            ping_menu()
        elif choice == "5" or choice.lower() == 'back':
            network_discovery_menu()
        elif choice.lower() == 'q' or choice.lower() == 'quit':
            sys.exit()


# Need to Change the Function Name
def option_1():
    username = input("Username to Query: ")
    #username = "aji"
    if username == "":
        username = "aji"

    checker = UserCheck(username)
    checker.username_check()


def network_discovery_menu():
    while True:
        display_network_menu()
        choice = input("Enter choice, 'back' to go back, or 'q' to quit\n>>> ")
        if choice == "1":
            ping_menu()
        elif choice == "2" or choice.lower() == 'back':
            main()
        elif choice.lower == 'q' or choice.lower() == 'quit':
            sys.exit()
    

# Main Function for Python Program
def main():
    # Catch CTRL-C and handle securely
    signal.signal(signal.SIGINT, signal_handler)    

    # Handle errors in Main Menu
    try:
        while True:
            display_main_menu()
            choice = input("Enter your choice ('q' to quit): ")

            if choice == '1':
                option_1()

            elif choice == '2':
                network_discovery_menu()

            elif choice.lower() == 'q':
                print("Goodbye")
                sys.exit(0)
            
            else:
                print("Invalid choice. Please choose one of the options or 'q' to quit.")

    except KeyboardInterrupt:
        print("\nKeyboard interrupt attempted.")
        sys.exit(1)


if __name__ == "__main__":
    main()