import argparse
import socket
import sys
import time

def port_check(port):
    if port.isdigit() and int(port) in range(1, 65536):
        return True
    else:
        return False


def parse_arguments():
    parser = argparse.ArgumentParser(description="Basic Ping scanner that allows for ICMP, TCP, and UDP.")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--icmp", help="TCP Scan", action="store_true")
    group.add_argument("-t", "--tcp", help="TCP Scan", action="store_true")
    group.add_argument("-u", "--udp", help="UDP Scan", action="store_true")

    parser.add_argument("-a", "--address", help="IP Address", required=True)
    parser.add_argument("-p", "--port", default=80, help="Port to use for TCP Ping")

    return parser.parse_args()


def icmp_ping(ip):

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.settimeout(1)
    s.sendto(b"", (ip, 1))

    try:
        resp, addr = s.recvfrom(1024)
        print(resp)
    except socket.timeout:
        resp = False
    finally:
        s.close()
        return resp


def tcp_ping(ip, port):
    try:
        start_time = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        resp = True
    except socket.error as e:
        resp = False
    
    finally:
        s.close()
    return resp


def udp_ping(ip):
    pass

def main():
    args = parse_arguments()
    ip = args.address
    port = args.port

    if not port_check(port):
        print("Make sure to your port is a number between 1 & 65535")
        sys.exit()

    if args.icmp:
        if icmp_ping(ip):
            print(f"{ip}")
        
    elif args.tcp:
        if tcp_ping(ip, int(port)):
            print(f"{ip} responded on port {port}")


main()