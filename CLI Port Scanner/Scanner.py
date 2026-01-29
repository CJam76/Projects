import socket

target = input("Enter the host to scan: ")

try:
    ip = socket.gethostbyname(target)

    min_port = int(input("Enter the first port to scan: "))
    max_port = int(input("Enter the last port to scan: "))

    for i in range(min_port,max_port + 1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)

        result = s.connect_ex((ip,i))

        open_ports = []
        closed_ports = []

        if result == 0:
            open_ports.append(i)
        else:
            closed_ports.append(i)

        for port in open_ports:
            print(str(port) + " is open")

        try:
         s.shutdown(socket.SHUT_WR)
        except OSError as e:
         print(f"Error during shutdown: {e}")
        finally:
            s.close()


except socket.gaierror:
    print("Could not resolve hostname.")


