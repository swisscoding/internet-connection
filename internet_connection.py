#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import socket

# decoration
print(stylize("\n---- | Check internet connection | ----\n", fg("red")))

# class
class Connection:
    def __init__(self):
        self.ip_address = socket.gethostbyname(socket.gethostname())

    # output magic method
    def __repr__(self):
        if self.ip_address == "127.0.0.1":
            return f"No internet connection, your localhost is {self.ip_address}.\n"
        else:
            return f"Internet connected with the IP address: {self.ip_address}\n"


# main execution
if __name__ == "__main__":
    print(Connection())
