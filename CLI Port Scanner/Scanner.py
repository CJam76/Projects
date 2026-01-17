import socket

target = input("Enter the host to scan: ")

# Return IP if valid host, otherwise return error message.

try:
    ip = socket.gethostbyname(target)
    print(f"Target IP: {ip}")
except socket.gaierror:
    print("Could not resolve hostname.")

# input target IP
# input port number
# create TCP socket
# set timeout
# attempt connect_ex
# if result == 0 → print open
# else → print closed
# close socket
ip = input("Enter the host ip: ")
port_number = int(input("Enter port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(1)

result = s.connect_ex((ip, port_number))
if result == 0:
    print("Port is open")
else:
    print("Port is closed")

try:
    s.shutdown(socket.SHUT_WR)
except OSError as e:
    print(f"Error during shutdown: {e}")
finally:
    s.close()
