import socket
HOST = socket.gethostbyname(socket.gethostname())              # Endereco IP do Servidor
PORT = 9999            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print(HOST)
while True:
    msg, cliente = udp.recvfrom(1024)
    print(msg)
udp.close()