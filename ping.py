import socket
import sys
import time

def port_check(port):
    if port.isdigit() and int(port) in range(1, 65536):
        return True
    else:
        return False


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

        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        resp = True
    except socket.error as e:
        resp = False
    
    finally:
        s.close()
    return resp


def udp_ping(ip):
    print("Coming Soon")